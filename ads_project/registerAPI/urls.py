from django.urls import path

from . import views

urlpatterns = [
    path('registers/', views.register, name='register'),
    path('login-member/', views.login, name='loginmember'),

]