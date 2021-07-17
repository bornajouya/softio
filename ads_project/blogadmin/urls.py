from django.urls import path

from . import views

urlpatterns = [
   path('', views.add, name='add'),
   path('addcontent/', views.addcontent, name='addcontent'),
]