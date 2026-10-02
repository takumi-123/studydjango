from django.urls import path
from . import views

app_name = 'accounts' # 他のフォルダにも同じ名前の関数が増えるかもしれないときの指定

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]