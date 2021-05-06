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
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render(request, 'user_login.html', context=RequestContext(request))


# @never_cache
def register(request):
    form = CreateUserForm()
    context = {'form': form}

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account was Created")
        else:
            # messages.error(request, "problem ")
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
                print(msg)
    return render(request, 'index.html', context=context)
