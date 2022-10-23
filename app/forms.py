from django import forms
from .models import *
class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        widgets = {
        'password': forms.PasswordInput
    }