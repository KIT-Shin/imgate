from django import forms
from .models import Imgate

class ImgateForm(forms.ModelForm):
    """
    新規データ登録画面用のフォーム定義
    """
    class Meta:
        model = Kakeibo
        fields = ['username', 'image']