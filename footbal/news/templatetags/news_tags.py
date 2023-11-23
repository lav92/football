from django import template
from news.models import Category

register = template.Library()


@register.inclusion_tag('news/category_list.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}
