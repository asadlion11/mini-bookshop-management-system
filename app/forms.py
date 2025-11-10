from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

# Signup Form
class CustomSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
