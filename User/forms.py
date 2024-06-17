from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    avatar = forms.ImageField(label='avatar')
    bio = forms.CharField()


