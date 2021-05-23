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
from adsAPI.models import Ads
import AdvancedHTMLParser


def login(request):
    return render(request, 'login.html')

def index(request):

    ads_list = list(Ads.objects.values())
    for x in ads_list:
        # print(type(x['description']))
        parser = AdvancedHTMLParser.AdvancedHTMLParser()

        print(type(parser.parseStr("<p>gfjhg</p>")))
        # x['description'] = '''<p>gfjhg</p>'''

    context ={"ads_list": ads_list}

    return render(request, 'index.html',context=context)

def login_member(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            # login(user)
            return redirect("index")
        else:
            messages.info(request,'username or password is incorrect')
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
            # email = form.cleaned_data.get('email')
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password,email=email)
            # login(request, user)
            return redirect("login")

    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form': form})