from django.urls import path
from . import views

app_name = 'chapp'

urlpatterns = [
    path('', views.chapp_index, name='index'),
]