from django.contrib.auth.forms import UserCreationForm
from .models import User, Book
from django import forms
from django.forms import ModelForm

# Signup Form - Model form with abastraction and using model
class CustomSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

# Login Form - built in Form that is not using q model
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

# Book From - model from using model
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'quantity']