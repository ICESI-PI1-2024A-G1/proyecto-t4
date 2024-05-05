from django.http import JsonResponse
from SistemaContableApp.models import  *
from SistemaContableApp.forms import *
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.db.models import Q  
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required

from SistemaContableApp.permissions import user_in_group


allowed_groups1 = ['Administrador', 'Líder', 'Gestor', 'Ventanilla única','Contable']
excluded_group1 = 'Solicitante'

 


@login_required(login_url='', redirect_field_name='next')
@user_in_group(allowed_groups1, excluded_group1)
def summaryOneStopShopView(request):

    """
    View function to display a summary of following objects based on various filters and search parameters.

    Parameters:
    - request: HTTP request object

    Returns:
    - Rendered template with following objects summary based on applied filters and search parameters.
    """

    queryset = Following.objects.all()
    
    query = request.GET.get('q')
    estado = request.GET.get('estado')
    tipo = request.GET.get('tipo')
    ordenar_por = request.GET.get("ordenar_por", None)
    fecha_creacion_inicio = request.GET.get('fecha_creacion_inicio')
    fecha_creacion_fin = request.GET.get('fecha_creacion_fin')
    fecha_cierre_inicio = request.GET.get('fecha_cierre_inicio')
    fecha_cierre_fin = request.GET.get('fecha_cierre_fin')
    

    if query:
        queryset = queryset.filter(
            Q(type__icontains=query) | Q(currentState__state__icontains=query) 
        )
    if estado:
        queryset = queryset.filter(currentState__state=estado)        
    if tipo:
        queryset = queryset.filter(type__icontains=tipo)
    
    if ordenar_por:
        queryset = queryset.order_by(ordenar_por)

    if fecha_creacion_inicio and fecha_creacion_fin:
        queryset = queryset.filter(
            creationDate__range=[fecha_creacion_inicio, fecha_creacion_fin]
        )
    if fecha_cierre_inicio and fecha_cierre_fin:
        queryset = queryset.filter(
            closeDate__range=[fecha_cierre_inicio, fecha_cierre_fin]
        )
        
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    followingData = Following.objects.all()
    try:
        followingData = paginator.page(page_number)
    except PageNotAnInteger:
        followingData = paginator.page(1)
    except EmptyPage:
        followingData = paginator.page(paginator.num_pages)
    
    queryset = Following.objects.none()
    
    tipos = Following.objects.values_list('type', flat=True).distinct()
    estados = State.objects.all()
    fechas_creacion = Following.objects.values_list('creationDate', flat=True).distinct()
    fechas_cierre = Following.objects.values_list('closeDate', flat=True).distinct()
    
    context = {
        'followingData': followingData,
        'estados': estados, 
        'tipos': tipos,  # Obtener los tipos únicos
        'fechas_creacion': fechas_creacion,
        'fechas_cierre': fechas_cierre,
    }
    
    return render(request, 'summaryOneStopShop.html', context)

@login_required(login_url='', redirect_field_name='next')
@user_in_group(allowed_groups1, excluded_group1)
def fullOneStopShopView(request):

    """
    View function to display a full view of all following objects and attached documents.

    Parameters:
    - request: HTTP request object

    Returns:
    - Rendered template displaying all following objects and attached documents.
    """

    followingData = Following.objects.all()
    states = State.objects.all()
    attachedDocuments = AttachedDocument.objects.all()

    return render(request, 'fullOneStopShop.html', {'followingData': followingData, 'files': attachedDocuments, 'states': states})

@login_required(login_url='', redirect_field_name='next')
@user_in_group(['Ventanilla única'], excluded_group1)
def oneStopShopFormView(request):

    """
    View function to handle the submission and display of the one-stop shop form and attached documents.

    Parameters:
    - request: HTTP request object

    Returns:
    - If request method is POST and form data is valid:
        - Redirects to the one-stop shop form view.
    - If request method is GET or form data is invalid:
        - Renders the one-stop shop form with attached document form.
    """

    if request.method == 'POST':
        oneStopShopForm = OneStopShopForm(request.POST)
        attachedDocumentForm = AttachedDocumentForm(request.POST, request.FILES)
        if oneStopShopForm.is_valid() and attachedDocumentForm.is_valid():
            following = oneStopShopForm.save()  
            attachedDocument = attachedDocumentForm.save(commit=False)
            attachedDocument.associatedFollowing = following 
            attachedDocument.save()
            messages.success(request, 'Formulario enviado con éxito.')
            return redirect('OneStopShopForm')  
        else:
            oneStopShopForm = OneStopShopForm()
            attachedDocumentForm = AttachedDocumentForm()
            messages.error(request, 'Error al enviar el formulario.')
            return render(request, 'oneStopShopForm.html', {'oneStopShopForm': oneStopShopForm, 'attachedDocumentForm': attachedDocumentForm})
    else:
        oneStopShopForm = OneStopShopForm()
        attachedDocumentForm = AttachedDocumentForm()
        return render(request, 'oneStopShopForm.html', {'oneStopShopForm': oneStopShopForm, 'attachedDocumentForm': attachedDocumentForm})


def updateState(request, following_id):
    # Obtener el objeto Following que deseas actualizar
    following = get_object_or_404(Following, id=following_id)
    description = request.POST.get('description')

    if request.method == 'POST':
        # Obtener el nuevo estado del formulario
        estado_edit = request.POST.get('estadoEdit')

        if estado_edit:
            try:
                # Obtener el objeto State correspondiente al nuevo estado
                new_state = State.objects.get(state=estado_edit)
                # Actualizar el campo currentState del objeto Following
                following.currentState = new_state
                # Guardar los cambios en la base de datos

                following.save()
                state_change = StateChange(following=following, state=new_state, description=description)
                state_change.save()
                messages.success(request, 'Estado actualizado con éxito.')
            except State.DoesNotExist:
                messages.error(request, 'El estado proporcionado no existe.')
        else:
            messages.error(request, 'No se proporcionó ningún estado.')

    

    return redirect('fullOneStopShop')  # Redirigir a la página principal


def changeHistory(request, following_id):
    following = Following.objects.get(pk=following_id)
    state_changes = StateChange.objects.filter(following=following)

    return render(request, 'changeHistory.html', {'following': following, 'state_changes': state_changes})

# Función para guardar comentarios en un objeto Following, "comentario de aprovación"
def approval_comment(request, following_id):
    if request.method == 'POST':
        following = get_object_or_404(Following, pk=following_id)
        approval_comment_text = request.POST.get('approval_comment', '')
        following.approvalComments = approval_comment_text
        following.save()
    return redirect('fullOneStopShop')

# Función para guardar comentarios en un objeto Following, "comentario de contabilidad"
def accounting_comment(request, following_id):
    if request.method == 'POST':
        following = get_object_or_404(Following, pk=following_id)
        accounting_comment_text = request.POST.get('accounting_comment', '')
        following.accountingComments = accounting_comment_text
        following.save()
    return redirect('fullOneStopShop')

# Función para editar y guardar el estado de aceptación en un objeto Following
def acceptance_state(request, following_id):
    if request.method == 'POST':
        following = get_object_or_404(Following, pk=following_id)
        acceptance_state_text = request.POST.get('acceptance_state', '')
        following.acceptanceState = acceptance_state_text  # Debería ser following.acceptanceState
        following.save()
    return redirect('fullOneStopShop')

# Función para editar y guardar el estado de revisión en un objeto Following
def revision_state(request, following_id):
    if request.method == 'POST':
        following = get_object_or_404(Following, pk=following_id)
        revision_state_text = request.POST.get('revision_state', '')
        following.revisionState = revision_state_text  # Debería ser following.acceptanceState
        following.save()
    return redirect('fullOneStopShop')

# Función para editar y guardar el estado de aprobación en un objeto Following
def approval_state(request, following_id):
    if request.method == 'POST':
        following = get_object_or_404(Following, pk=following_id)
        approval_state_text = request.POST.get('approval_state', '')
        following.approvalState = approval_state_text  # Debería ser following.acceptanceState
        following.save()
    return redirect('fullOneStopShop')