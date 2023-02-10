from django.db import models

class MyModel(models.Model):
    '''画像保存テストモデル'''
    # 画像カラム
    col1 = models.ImageField(
        upload_to='images/', # imagesフォルダに入れる
    )
