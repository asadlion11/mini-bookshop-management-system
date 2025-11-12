from django.shortcuts import render, redirect
from app.forms import CustomSignupForm , LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# Signup views
def signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = CustomSignupForm()
    return render(request, 'app/signup.html', {'form': form})
        
# Login views
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    form = LoginForm()
    return render(request, 'app/login.html', {'form': form})
                

# Logout views
def logout_user(request):
    logout(request)
    return redirect('login')

# dashboard views
@login_required
def dashboard(request):
    username = request.user.username
    return render(request, 'app/dashboard.html', {'username': username})