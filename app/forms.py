from dataclasses import field
from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        # widgets = {
        # 'password': forms.PasswordInput
    # } 
        fields= '__all__'
    

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        