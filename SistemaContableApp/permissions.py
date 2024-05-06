from django.contrib import messages
from django.shortcuts import redirect

def user_in_group(allowed_groups, excluded_group):
    """
    Decorator for views that checks if the user is in one of the specified allowed groups, but not in the excluded group.
    If the user is authenticated and meets the group requirements, the view is executed.
    If the user is authenticated but does not meet the group requirements, a Django message is displayed, and the user remains on the same page.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and (
                request.user.groups.filter(name__in=allowed_groups).exists() and
                not request.user.groups.filter(name=excluded_group).exists()
            ):
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'No tienes los permisos requeridos')
                return redirect(request.META.get('HTTP_REFERER', 'home'))
        return _wrapped_view
    return decorator