from django.contrib import admin
from django.contrib.admin import register

from news.models import News, Category, Tag


@register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['pk', 'title', 'created_at', 'category', 'views', 'author']
    list_display_links = ['pk', 'title']
    readonly_fields = ['views', 'author']
    list_per_page = 10
    list_filter = ['category', 'author']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'description']


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


