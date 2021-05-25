from django.shortcuts import render
import requests
from django.views.decorators.cache import never_cache
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import *
from django.shortcuts import redirect
from django.template import RequestContext
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import AdvancedHTMLParser


def detail_view(request,id):


    ads_ins = list(Ads.objects.values().filter(id=id))[0]

    context ={"ads_ins": ads_ins}
    print(ads_ins)
    print(type(ads_ins))


    print(id)
    return render(request, 'detail.html',context=context)