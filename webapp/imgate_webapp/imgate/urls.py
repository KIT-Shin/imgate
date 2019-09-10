from django.shortcuts import render
from django.urls import path
from django.contrib.auth.views import logout
from django.conf.urls import url

from . import views

app_name = 'imgate'

urlpatterns = [
    path('imgate_list/', views.ImgateListView.as_view(), name='imgate_list'),
    path('create/',views.Create_account.as_view(), name='create'),
    path('imgate_login/', views.AccountLogin.as_view(), name='imgate_login'),
    path('imgate_mypage/', views.render_mypage, name='imgate_mypage'),
    path('', views.Top.as_view(), name='top'),
    # path('login/', views.AccountLogin.as_view(), name='imgate_login'),
    # path('logout/', views.Logout.as_view(), name='logout'),
    path('logout/', logout, {'template_name': 'imgate/top.html'}, name='logout'),
    path('index/', views.index, name='index'),
]
