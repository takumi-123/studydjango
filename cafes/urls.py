from django.urls import path
from .views import cafe_list, SignUpView  # インポートはそのまま

urlpatterns = [
    path('', cafe_list, name='cafe_list'),             # views. を取ってスッキリさせる
    path('signup/', SignUpView.as_view(), name='signup'),  # SingUpView のスペルミスを修正
]