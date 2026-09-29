from django.urls import path
from .views import cafe_list, SignUpView, cafe_new, cafe_edit, cafe_delete # インポートはそのまま

urlpatterns = [ # path(住所, views.pyの関数, 名前)
    path('', cafe_list, name='cafe_list'),             # views. を取ってスッキリさせる
    path('signup/', SignUpView.as_view(), name='signup'),  # SingUpView のスペルミスを修正
    path('cafe/new/', cafe_new, name='cafe_new'),

    # 編集と削除
    path('cafe/<int:pk>/edit/', cafe_edit, name='cafe_edit'),
    path('cafe/<int:pk>/delete/', cafe_delete, name='cafe_delete'),
]
