from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="本のタイトル")
    author = models.CharField(max_length=100, verbose_name="著者名")
    rating = models.IntegerField(default=3, verbose_name="評価(1~5)")
    review = models.TextField(blank=True, verbose_name="感想")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")

    def __str__(self):
        return self.title