from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import chat
from registerAPI.models import User
from adsAPI.models import Ads 
from django.views.decorators.csrf import csrf_exempt
    
# Create your views here.

#def send_msg(request):

def Chat_View(request,id):
    ''' this function should register the message of each part and show them inside of detail page'''
    if request.POST:    
        text = request.POST.get('text')
        user = User.objects.get(username=request.user)
        print (user)
        ads = Ads.objects.get(id=id)
        new_msg = chat(text=text,user = user, ads=ads)

        if  Ads.objects.filter(user__username=user,id=id).exists():
            new_msg.isfirst = True
            chat.save(new_msg)
        else:
            chat.save(new_msg)
            #return detail_view(request,id)
        
        #return HttpResponse(500)
    #else:
        #return HttpResponse(600)

#def Chat_View(request,id):
    print(Ads.objects.values().filter(id=id))
    if chat.objects.values().filter(ads=Ads.objects.values().filter(id=id)[0]['id']):
        this_chat = chat.objects.values().filter(ads=Ads.objects.values().filter(id=id)[0]['id'])
    else:
        this_chat = None
       
    return this_chat
