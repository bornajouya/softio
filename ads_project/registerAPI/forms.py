from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'type': 'username','placeholder':'username'}),
            'email': forms.TextInput(attrs={'type': 'email','placeholder':'E-mail'}),
            'password1': forms.TextInput(attrs={'type': 'password','placeholder':'password'}),
            'password2': forms.TextInput(attrs={'type': 'password','placeholder':'re-try password'}),

        }
