from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import chapp_Message

# Create your views here.
@login_required # ログインしている人だけ見れる
def chapp_index(request):
    # POSTリクエスト
    if request.method == "POST":
        # フォームに入力された分をcontentに取り出す
        content = request.POST.get('content')
        # 中身が空ならデータベースにほぞん
        if content:
            chapp_Message.objects.create(
                user=request.user, #今ログインしてるゆーざー
                content=content # 入力されたてきすと
            )
        return redirect('chapp:index')

    # GETリクエスト
    # データベースにすべてのメッセージを取り出し古い順に並び替える
    messages = chapp_Message.objects.all().order_by('created_at')
    # HTMLの辞書データ
    content = {'message': messages,}

    return render(request, 'chapp/index.html', content)