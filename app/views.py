from django.shortcuts import render

# Create your views here.

# Login views
def login(request):
    return render(request, 'app/login.html')

# Signup views
def signup(request):
    return render(request, 'app/signup.html')

# Logout views
def logout(request):
    pass