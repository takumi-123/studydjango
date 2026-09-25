from django.db import models

# Create your models here.

class Cafe(models.Model): 
    # CharField:短い名前、文字, InterField:整数, TextFild:本文や長めの乾燥, 
    name = models.CharField(max_length=100, verbose_name='店名')
    area = models.CharField(max_length=100, verbose_name='エリア')
    genre = models.CharField(max_length=100, verbose_name='ジャンル', blank=True, null=True)
    rating = models.IntegerField(verbose_name='評価(1~5)', default=3)
    recommend_menu = models.CharField(max_length=100, verbose_name='おすすめメニュー')
    memo = models.TextField(verbose_name='感想、メモ', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='登録日時')

    def __str__(self):
        return self.name