from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = "category"


    #カラム名の定義
    category_name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.category_name

class Imgate(models.Model):
   class Meta:
       #テーブル名
       db_table ="Imgate"

   #カラムの定義
   username = models.CharField(verbose_name="名前")
   image = models.CharField(verbose_name="イメージ")

   def __str__(self):
       return self.memo