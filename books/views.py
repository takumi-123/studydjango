from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # ← 追加
from .models import Book
from .forms import BookForm

# Create your views here.
@login_required  # ログイン中のみ
def book_list(request):
    # ログインしているユーザーの本だけを取得
    books = Book.objects.filter(user=request.user)
    return render(request, 'books/book_list.html', {'books': books})

# 新規作成
@login_required  # ログイン中のみ
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            # DBに保存する前に、user（誰が登録したか）を自動でセットする
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('books:book_list')  # 名前空間つきのURLにリダイレクト
    else:
        form = BookForm()

    return render(request, 'books/book_form.html', {'form': form})