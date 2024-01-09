from django import template

from shop.models import Category

register = template.Library()


@register.inclusion_tag('shop/include/category_clouds.html')
def show_category_clouds():
    cats = Category.objects.all()
    return {'cats': cats}
