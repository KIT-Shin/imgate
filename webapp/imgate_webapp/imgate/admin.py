from django.contrib import admin

# Register your models here.
from .models import Imgate

#追加
class ImgateAdmin(admin.ModelAdmin):
    list_display=('username','image')


admin.site.register(Imgate,ImgateAdmin)