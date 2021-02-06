from django import forms
from .models import Profile, Project
from django.contrib.auth.models import User
from django.contrib.auth.forms import 


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']