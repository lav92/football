from django.contrib import admin
from django.contrib.admin import register

from news.models import News

@register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

