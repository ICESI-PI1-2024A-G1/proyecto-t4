from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json

@login_required
def get_users(request):
    exclude = json.loads(request.GET.get('exclude', '{}'))
    users_query = User.objects.all()

    if 'gestor' in exclude and exclude['gestor']:
        users_query = users_query.exclude(id=exclude['gestor'])

    if ('aprobador' in exclude and exclude['aprobador']) or ('revisor' in exclude and exclude['revisor']):
        users_query = users_query.exclude(id__in=[exclude.get('aprobador'), exclude.get('revisor')])

    users = users_query.values('id', 'first_name', 'last_name')
    return JsonResponse(list(users), safe=False)