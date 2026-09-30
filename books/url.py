from django.urls import path
from .views import book_list

urlpatterns = [
    # http://a27.0.0.1.8000/books
    path('', book_list, name='book_list'),
]