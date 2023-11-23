from django.shortcuts import render, HttpResponse
from django.views.generic import ListView

from news.models import News


class HomePage(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    extra_context = {
        'title': 'Main Page',
    }

def single_news(request, news_slug):
    return HttpResponse('single post')
