from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login-member/', views.login_member),

]