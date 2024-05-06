from django.http import JsonResponse
from SistemaContableApp.models import User 
from django.contrib.auth.decorators import login_required
import json

@login_required
def get_users(request):
    """
    View to get a list of users excluding the specified users.

    Args:
        request (HttpRequest): The received HTTP request.

    Returns:
        JsonResponse: A JSON response with a list of dictionaries containing the 'id', 'first_name', and 'last_name' fields of the users.
    """
    exclude = json.loads(request.GET.get('exclude', '{}'))
    try:
        users_query = User.objects.all()  # Accede al queryset de User
        if 'gestor' in exclude and exclude['gestor']:
            users_query = users_query.exclude(id=exclude['gestor'])
        if 'aprobador' in exclude and exclude['aprobador']:
            users_query = users_query.exclude(id=exclude['aprobador'])
        if 'revisor' in exclude and exclude['revisor']:
            users_query = users_query.exclude(id=exclude['revisor'])

        users = users_query.values('id', 'name', 'last_name')  # Usa 'name' y 'last_name', que son los campos de tu modelo
        return JsonResponse(list(users), safe=False)
    except Exception as e:
        return JsonResponse({'error': 'Error fetching users'}, status=500)