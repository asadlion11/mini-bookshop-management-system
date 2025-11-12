from django.shortcuts import render, redirect
from app.forms import CustomSignupForm , LoginForm, BookForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book
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
    full_name = request.user.get_full_name()
    books = Book.objects.all().count()
    current_user_added_books = Book.objects.filter(user=request.user).count()
    other_users_added_books = Book.objects.exclude(user=request.user).count()
    
    return render(request, 'app/dashboard.html', {'full_name': full_name, 'books': books, 'current_user_added_books': current_user_added_books, 'other_users_added_books': other_users_added_books})

# books view
@login_required
def books(request):
    books = Book.objects.all()
    current_user_added_books = Book.objects.filter(user=request.user)
    return render(request, 'app/books.html', {'books': books, 'current_user_added_books': current_user_added_books})

# new book views
@login_required
def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('books')
    form = BookForm()
    return render(request, 'app/book-form.html', {'form': form})
    
   
@login_required
def update_book(request):
    pass

@login_required
def delete_book(request):
    pass