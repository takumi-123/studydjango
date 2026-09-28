# ブラウザに入力欄を表示したり送られたのか正しいか
from django import forms # Djangoのフォーム機能
from .models import Cafe # cafesフォルダーのmodels.pyのDBもってくる

class CafeForm(forms.ModelForm): # 新しいフォームのクラス（設計図）の名前を CafeForm として作ります
    class Meta: # 設定データをまとめるくらす
        model = Cafe # インポートした Cafe モデル（データベースの設計図）をベースにするよ、と指定しています
        fields = ['name'] # 入力フォームには、とりあえず『名前』のテキストボックスだけ置いてね」という指示です