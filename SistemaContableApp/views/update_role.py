from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from SistemaContableApp.models import Following
from django.contrib.auth.models import User

@require_POST
@csrf_exempt
def update_role(request):
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
        return JsonResponse({"success": False, "message": str(e)})
