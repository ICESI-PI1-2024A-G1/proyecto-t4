from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from SistemaContableApp.models import  *
from django.shortcuts import render, get_object_or_404, redirect
from SistemaContableApp.forms import *
from SistemaContableApp.permissions import user_in_group

allowed_groups1 = ['Administrador']
excluded_group1 = 'Solicitante'


@login_required(login_url='', redirect_field_name='next')
@user_in_group(allowed_groups1, excluded_group1)
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_required(login_url='', redirect_field_name='next')
@user_in_group(allowed_groups1, excluded_group1)
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')  
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'update_user.html', {'form': form})

