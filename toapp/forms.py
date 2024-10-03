from django import forms
from django.contrib.auth.models import User
from .import models
from .models import Customer

class CustomerUserform(forms.ModelForm):
    
    class Meta:
        model= User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ("addres", 'mobile','profile_pic')

        