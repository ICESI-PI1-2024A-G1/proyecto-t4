from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from SistemaContableApp.models import Following
from SistemaContableApp.models import User
from SistemaContableApp.permissions import user_in_group
from django.contrib.auth.decorators import login_required

allowed_groups1 = ['Administrador', 'Líder', 'Gestor']
excluded_group1 = 'Solicitante'

 

@require_POST
@csrf_exempt
@login_required(login_url='', redirect_field_name='next')
@user_in_group(allowed_groups1, excluded_group1)
def update_role(request):
    
    """
    View to update the role (manager, acceptor, or reviewer) of a user for a specific following.

    Args:
        request (HttpRequest): The received HTTP request.

    Returns:
        JsonResponse: A JSON response with a success status and a message.
    """
    try:
        following_id = request.POST.get('following_id')
        user_id = request.POST.get('user_id')
        role_type = request.POST.get('role_type')
        
        following = Following.objects.get(id=following_id)
        user = User.objects.get(id=user_id)
        
        if role_type == 'gestor':
            following.manager = user.username  # Usa el username del usuario
        elif role_type == 'aprobador':
            following.acceptor = user.username  # Usa el username del usuario
        elif role_type == 'revisor':
            following.revisor = user.username  # Usa el username del usuario
        
        following.save()
        return JsonResponse({"success": True, "message": "Usuario asignado correctamente."})
    except Exception as e:
        pass
