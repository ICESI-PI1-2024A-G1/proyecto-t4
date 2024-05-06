from django.contrib.auth.models import User
from django.shortcuts import render
from ..forms import AsignarGestorForm

def asignar_gestor(request):
    usuarios = User.objects.all()  
    if request.method == 'POST':
        form = AsignarGestorForm(request.POST)
        if form.is_valid():
            gestor_seleccionado = form.cleaned_data['gestor']
            # Aquí puedes manejar la asignación del gestor
            # Por ejemplo, puedes guardar el gestor en el modelo correspondiente
            return render(request, 'Users.html', {'form': form, 'success_message': 'Gestor asignado correctamente', 'usuarios': usuarios})
    else:
        form = AsignarGestorForm()

    return render(request, 'Users.html', {'form': form, 'usuarios': usuarios})
