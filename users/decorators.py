from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def logged_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'user' or group == 'admin':
            return view_func(request, *args, *kwargs)

        if not group:
            return redirect('login')

    return wrapper_func

def notlogged_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'user' or group == 'admin':
            return redirect('index')

        if not group:
            return view_func(request, *args, *kwargs)

    return wrapper_func

