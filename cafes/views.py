from django.shortcuts import render, redirect, get_object_or_404 # redirectとrenderを呼び出す
from django.contrib.auth.forms import UserCreationForm # 新しいユーザーを作るフォームを呼び出す
from django.urls import reverse_lazy # URLを名前からぱすしてくれます
from django.views.generic import CreateView # djangoがデータを新しく作成、保存するための型
from .models import Cafe # models. cafeのDBをもってくる
from .forms import CafeForm

# Create your views here.

# カフェ一覧表示をする処理
def cafe_list(request):
    # データベースから全てのカフェデータを取得する models.pyから
    cafes = Cafe.objects.all()

    # 取得したデータをHTMLに渡して表示する
    return render(request, 'cafes/cafe_list.html', {'cafes': cafes})


# 新しくカフェを登録する処理
def cafe_new(request):
    if request.method == "POST": # POSTリクエストなら
        form = CafeForm(request.POST) # 入力されたデータをフォームに詰め込む
        if form.is_valid(): # 正しければDBに保存
            form.save() # 正しければ保存
            return redirect('cafe_list') # 一覧に移動する
    else: #GETなら
        form = CafeForm() #空っぽのフォームを用意する 
    return render(request, 'cafes/cafe_edit.html', {'form': form}) #登録画面へ移動
# 新規ユーザー登録ビュー
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # 登録できたらログイン画面へ移動
    template_name = 'cafes/signup.html'

# 編集ビュー
def cafe_edit(request, pk):
    # データべスカラ指定されたIDのファイルのカフェを探すなければ404エラー
    cafe = get_object_or_404(Cafe, pk=pk) # pk=主キー(DJANGOが勝手にidをAUTO_INCREMENTしてる)

    if request.method == "POST":
        # もとからあるmodels.pyのcafe.DBをユーザの新しいPOSTにかえる
        form = CafeForm(request.POST, instance=cafe)
        if form.is_valid(): # DB正しいなら
            form.save() # 保存
            return redirect('cafe_list')
    else:
        # GETなら既存のでーたをフォームにセット
        form = CafeForm(instance=cafe)
    return render(request, 'cafes/cafe_edit.html', {'form': form, 'cafe': cafe})

# 削除
def cafe_delete(request, pk):
    # データベースあるか探す
    cafe = get_object_or_404(Cafe, pk=pk)

    if request.method == "POST":
        #削除
        cafe.delete() 
        return redirect('cafe_list')

    # 確認画面表示
    return render(request, 'cafes/cafe_confirm_delete.html', {'cafe': cafe})