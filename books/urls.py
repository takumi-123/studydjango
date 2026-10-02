from django.urls import path
from .views import book_list, book_create

urlpatterns = [
    # http://127.0.0.1.8000/books
    path('', book_list, name='book_list'),
    path('add/', book_create, name='book_create'), # 作成
]