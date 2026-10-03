from django.db import models
from django.conf import settings

# Create your models here.
class chapp_Message(models.Model):
    # 誰が投稿したかUserモデルとひもずけ（django
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='ユーザー名')
    # メッセージ本文
    content = models.TextField(verbose_name='メッセージ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')

    def __str__(self):
        # ターミナルでユーザー名、本文20文字で返す
        return f'{self.user.username}: {self.content[:20]}'