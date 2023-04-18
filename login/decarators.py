from django.http import HttpResponse
from django.shortcuts import render

def allowed_users(allowed_roles=[]):
    def decarator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return render(request,'404/404.html')
        return wrapper_func
    return decarator