from django.contrib import admin

# Register your models here.
from .models import Category, Imgate

admin.site.register(Category)
admin.site.register(Imgate)