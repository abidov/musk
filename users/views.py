from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, logged_only, notlogged_only

# Create your views here.
@logged_only
def index(request):
    return render(request, 'home/index.html', {})

@logged_only
def userPage(request):
    return render(request, 'accounts/user.html', context={})

@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='user')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    return render(request, 'accounts/register.html', context={'form': form})

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'accounts/login.html', context={})

def logoutUser(request):
    logout(request)
    return redirect('index')