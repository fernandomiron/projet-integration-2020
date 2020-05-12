from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None #if user is a part of the group

            #if a list of group actually exist who want set the group value
            #to first term on the list.
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Vous n'êtes pas autorisé à cette page")
        return wrapper_func
    return decorator
