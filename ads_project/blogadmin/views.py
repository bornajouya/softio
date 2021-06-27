from django.shortcuts import render
from adsAPI.models import Ads


# Create your views here.
def add(request):
    # ads_ins = list(Ads.objects.values().filter(id=id))[0]

    # context = {
    #     "ads_ins": ads_ins,
    #     "this_chat": Chat_View(request, id)
    # }
    # print('this is un updated context %s' % context)
    # # chat_context= Chat_View(request,id)
    # # print('this is chat %s' % chat_context)
    # # context = context.update(chat_context)
    # print('this is %s context' % context)

    context = {"ads_list": list(Ads.objects.all().filter(user=request.user).values())}
    # Add your context here

    return render(request, 'add.html', context=context)
