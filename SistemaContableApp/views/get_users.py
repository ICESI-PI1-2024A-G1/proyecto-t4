from django.http import JsonResponse
from django.contrib.auth.models import User
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
    users_query = User.objects.all()

    if 'gestor' in exclude and exclude['gestor']:
        users_query = users_query.exclude(id=exclude['gestor'])

    if ('aprobador' in exclude and exclude['aprobador']) or ('revisor' in exclude and exclude['revisor']):
        users_query = users_query.exclude(id__in=[exclude.get('aprobador'), exclude.get('revisor')])

    users = users_query.values('id', 'first_name', 'last_name')
    return JsonResponse(list(users), safe=False)