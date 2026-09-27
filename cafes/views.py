from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Cafe

# Create your views here.

# カフェ一覧表示をする処理
def cafe_list(request):
    # データベースから全てのカフェデータを取得する models.pyから
    cafes = Cafe.objects.all()

    # 取得したデータをHTMLに渡して表示する
    return render(request, 'cafes/cafe_list.html', {'cafes': cafes})

# 新規ユーザー登録ビュー
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # 登録できたらログイン画面へ移動
    template_name = 'cafes/signup.html'