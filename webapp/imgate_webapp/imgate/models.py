from django.db import models

# Create your models here.

class Imgate(models.Model):
   class Meta:
       #テーブル名
       db_table ="Imgate"
       app_label = 'Imgate'

   #カラムの定義
   username = models.CharField(verbose_name="名前")
   image = models.CharField(verbose_name="イメージ")



   def __str__(self):
       return self.memo