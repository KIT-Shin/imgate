from django import forms
from .models import Imgate

from django.contrib.auth.forms import (
    AuthenticationForm
)


class ImgateForm(forms.ModelForm):
    """
    新規データ登録画面用のフォーム定義
    """
    class Meta:
        model = Imgate
        fields = ['username', 'image']


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label #placeholderにフィールドのラベルを入れる