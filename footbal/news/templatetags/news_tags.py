from django import template
from news.models import Category, News, Tag

register = template.Library()


@register.inclusion_tag('news/include/category_list.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}


@register.inclusion_tag('news/include/popular_news.html')
def popular_news():
    news = News.objects.all().order_by('-views')[:5]
    return {'news': news}


@register.inclusion_tag('news/include/tag_clouds.html')
def tag_clouds():
    tags = Tag.objects.all()
    return {'tags': tags}


@register.inclusion_tag('news/include/sidebar-categories.html')
def sidebar_categories():
    cats = Category.objects.all()
    return {'cats': cats}
