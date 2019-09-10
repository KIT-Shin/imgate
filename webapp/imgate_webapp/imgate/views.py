from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from . forms import UserCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic, View
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

class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'create.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'create.html', {'form': form,})


create_account = Create_account.as_view()


class AccountLogin(View):
    """ログインページ"""
    def post(self, request, *arg, **kwargs):

        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {'form': form, })


    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form, })

account_login = AccountLogin.as_view()

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name ='imgate/top.html'