from django.shortcuts import render
import requests
from django.views.decorators.cache import never_cache
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# @never_cache
def register(request):
    form = CreateUserForm()
    context = {'form': form}

    if request.method == 'post':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'index.html', context=context)
