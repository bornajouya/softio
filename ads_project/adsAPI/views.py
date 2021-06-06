from django.shortcuts import render
from django.urls.conf import path
import requests
from django.views.decorators.cache import never_cache
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import *
from django.shortcuts import redirect
from django.template import RequestContext, context
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import AdvancedHTMLParser
from chatAPI.views import Chat_View
from django.views.decorators.csrf import csrf_exempt


def register_ads(request):
    title = request.POST.title
    describtion = request.POST.describtion
    user = request.User
    photo = request.POST.photo

    new_post = Ads(title,describtion,user,photo)
    Ads.save(new_post)

    context = {
        'context' : "thanks for your posting advertisment on our website."
    }
    return render(request, 'detail.html', context=context)



def detail_view(request,id):


    ads_ins = list(Ads.objects.values().filter(id=id))[0]

    context ={
        "ads_ins": ads_ins,
        "this_chat": Chat_View(request,id) 
        }
    print('this is un updated context %s' % context)
    #chat_context= Chat_View(request,id)
    #print('this is chat %s' % chat_context)
    #context = context.update(chat_context)
    print('this is %s context' % context)

    
    return render(request, 'detail.html',context=context)