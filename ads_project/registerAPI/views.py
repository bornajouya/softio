from django.shortcuts import render
import requests
from django.views.decorators.cache import never_cache
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.http import *
from django.shortcuts import redirect
from django.template import RequestContext
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def login_member(request):
    # logout(request)
    # username = password = ''
    # if request.POST:
    #     username = request.POST['username']
    #     password = request.POST['password']
    #
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         if user.is_active:
    #             login(request, user)
    #             return HttpResponseRedirect('/main/')
    return render(request, 'login.html')


# @never_cache
def register(request):
    form = CreateUserForm()
    context = {'form': form}

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(str(request.POST['password1']))
        print(str(request.POST['password2']))
        if form.is_valid():
            form.save()
            messages.success(request, "Account was Created")
            redirect("./login-member")
        else:
            messages.error(request, "Your password can’t be too similar to your other personal information. ")
            messages.error(request, "Your password must contain at least 8 characters. ")
            messages.error(request, "Your password can’t be a commonly used password. ")
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
                print(msg)
    return render(request, 'register.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})