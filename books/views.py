from django.shortcuts import render
from .models import Book

# Create your views here.
def book_list(request):
    # 1.データベースから全ての本データを取得するmodelsも変数.object.all()
    books = Book.objects.all()

    # 2.テンプレートに渡す辞書データを作る
    context = {'books': books}

    # テンプレートを書いてブラウザに返す
    return render(request, 'books/book_list.html', context)S