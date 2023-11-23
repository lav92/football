from django.shortcuts import render, HttpResponse
from django.views.generic import ListView

from news.models import News, Category


class HomePage(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    extra_context = {
        'title': 'Main Page',
    }


class SingleCategory(ListView):
    model = Category
    template_name = 'news/index.html'
    context_object_name = 'news'


def single_news(request):
    return HttpResponse('flwfjwef')
