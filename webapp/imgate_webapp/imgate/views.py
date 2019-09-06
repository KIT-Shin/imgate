from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Category, Imgate

#一覧表示用のDjango標準ビュー(ListView)を承継して一覧表示用のクラスを定義
class ImgateListView(ListView):
   #利用するモデルを指定
   model = Imgate
   #データを渡すテンプレートファイルを指定
   template_name = 'imgate/imgate_list.html'

   #家計簿テーブルの全データを取得するメソッドを定義
   def queryset(self):
       return Imgate.objects.all()