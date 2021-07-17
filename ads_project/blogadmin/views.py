from django.shortcuts import render
from adsAPI.models import Ads
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages

# Create your views here.
def add(request):


    context = {"ads_list": list(Ads.objects.all().filter(user=request.user).values())}
    # Add your context here

    return render(request, 'add.html', context=context)

@csrf_exempt
def addcontent(request):
    # logout(request)
    if request.POST:
        ads_name = request.POST.get('ads_name',False)
        description = request.POST.get('description',False)
        print(request)
        print(request.POST['ads_name'])
        print(request.POST['description'])
        # description = request.POST['description']

        # try:
        ads_ins = Ads(title=str(ads_name), description=description,user=request.user)
        ads_ins.save()
        return redirect("index")

        # except Exception as ex :
        #     messages.info(request, 'username or password is incorrect')

    return redirect("index")


