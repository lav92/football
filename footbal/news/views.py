from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from news.models import News, Category


class HomePage(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    extra_context = {
        'title': 'Main Page',
    }


class SingleCategory(ListView):
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.get(slug=self.kwargs['cat_slug'])
        context['title'] = cat.name
        return context

    def get_queryset(self):
        return News.objects.filter(category__slug=self.kwargs['cat_slug']).order_by('-created_at')


class SingleNews(DetailView):
    template_name = 'news/single-news.html'
    context_object_name = 'news'
    slug_url_kwarg = 'news_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = News.objects.get(slug=self.kwargs[self.slug_url_kwarg])
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(News, slug=self.kwargs[self.slug_url_kwarg])
