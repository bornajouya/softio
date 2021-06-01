

from django.urls import path,re_path

from . import views

urlpatterns = [

    # re_path(r'(?P<id>\w+)/(?P<slug>[\w-]+)/$', views.detail),
    re_path(r'ads/(?P<id>\w+)/$', views.detail_view, name='detail_view'),

]