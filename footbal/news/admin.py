from django.contrib import admin
from django.contrib.admin import register

from news.models import News, Category, Tag


@register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['pk', 'title', 'created_at', 'category', 'views', 'photo']
    list_display_links = ['pk', 'title']


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'description']


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


