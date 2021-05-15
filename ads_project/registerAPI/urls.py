from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('signup/', views.signup, name='signup'),
    path(r'^login/$', views.login, {'template_name': 'login.html'}, name='login'),
    path(r'', views.index, name='index'),

    path('login-member/', views.login_member),

]