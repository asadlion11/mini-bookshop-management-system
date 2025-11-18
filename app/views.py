from django.shortcuts import render, redirect
from app.forms import CustomSignupForm , LoginForm, BookForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book
from django.db.models import Sum
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
    books_types = Book.objects.all().count()
    total_books = Book.objects.all().aggregate(total=Sum('quantity'))['total']
    max_quantity_book = Book.objects.order_by('-quantity').first()
    highest_price_book = Book.objects.order_by('-price').first()
    lowest_price_book = Book.objects.order_by('price').first()
  
    
    return render(request, 'app/dashboard.html', {'full_name': full_name, 'books_types': books_types, 'total_books': total_books, 'max_quantity_book': max_quantity_book, 'highest_price_book': highest_price_book, 'lowest_price_book': lowest_price_book})

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
    
# update book
@login_required
def update_book(request, id):
    pass

@login_required
def delete_book(request):
    pass