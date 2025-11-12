from app import views
from django.urls import path

urlpatterns = [
    path('', views.login_user, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('books/', views.books, name='books'),
    path('books/new-book', views.new_book, name='new-book'),
    path('books/update-book/<int:id>', views.update_book, name='update-book'),
    path('books/delete-book/<int:id>', views.delete_book, name='delete-book'),
]
