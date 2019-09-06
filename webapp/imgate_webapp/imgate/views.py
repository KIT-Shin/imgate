from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import LoginForm

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Imgate

#一覧表示用のDjango標準ビュー(ListView)を承継して一覧表示用のクラスを定義
class ImgateListView(ListView):
   #利用するモデルを指定
   # model = Imgate
   #データを渡すテンプレートファイルを指定
   template_name = 'imgate/imgate_list.html'

   #画像テーブルの全データを取得するメソッドを定義
   def queryset(self):
       return None#Imgate.objects.all()

class ImgateLogin(ListView):
    # model = Imgate
    template_name = 'imgate/imgate_login.html'

    def queryset(self):
       return render(self, 'imgate/imgate_login.html')

    #def imgate_mypage(request):
      # return render(request, 'imgate/imgate_mypage.html')

class ImgateMypage(ListView):

    template_name = 'imgate/imgate_mypage.html'

    def queryset(self):
        return render(self, 'imgate/imgate_mypage.html')

def render_login(request):
    return render(request,"imgate/imgate_login.html")

def render_mypage(request):
    return render(request,"imgate/imgate_mypage.html")


class Top(generic.TemplateView):
    template_name = 'imgate/top.html'

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'imgate/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name ='imgate/top.html'