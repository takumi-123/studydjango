from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.
def book_list(request):
    # 1.データベースから全ての本データを取得するmodelsも変数.object.all()
    books = Book.objects.all()

    # テンプレートを書いてブラウザに返す (リクエスト,html名, 変数のなまえ)
    return render(request, 'books/book_list.html', {'books': books})

# 新規作成
def book_create(request):
    if request.method == "POST": # POSTなら
        form = BookForm(request.POST) # POSTから送信データをいれて送信されたフォームを変数form作る
        if form.is_valid(): # 入力されたフォームが正しいかチェック
            form.save() #DBに保存
            return redirect('book_list')
    else:
        form = BookForm() #空のフォーム

    return render(request, 'books/book_form.html', {'form': form})