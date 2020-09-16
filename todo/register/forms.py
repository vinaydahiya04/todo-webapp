from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import MyUser

class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField()   

    class Meta:
        model = User
        fields = ['username','email','password']

class UserExtraForm(forms.ModelForm):
    class Meta():
        model = MyUser
        fields = ('profile_pic',)

        

