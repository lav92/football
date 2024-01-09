from django.contrib import admin
from django.contrib.admin import register

from shop.models import Category, Goods, Cart


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['name']


@register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'stock', 'available', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['name', 'pk']
    list_filter = ['category', 'available']
    list_per_page = 10


@register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'goods', 'quantity')
    list_display_links = ['pk', 'user']
    list_per_page = 15
