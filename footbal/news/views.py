from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import F
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from news.models import News, Category, Tag
from news.forms import AddNewsForm
from news.serializer import NewsSerializer

from django.core.cache import cache


def video(request):
    return render(request, 'news/video.html')


class HomePage(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    extra_context = {
        'title': 'Main Page',
    }
    paginate_by = 3

    def get_queryset(self):
        result = cache.get('news_set')
        if not result:
            result = News.objects.select_related('category', 'author').prefetch_related('tag').all()
            cache.set('news_set', result, 30)
        return result


class SingleCategory(ListView):
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.get(slug=self.kwargs['cat_slug'])
        context['title'] = cat.name
        return context

    def get_queryset(self):
        return News.objects.select_related('category', 'author').prefetch_related('tag')\
            .filter(category__slug=self.kwargs['cat_slug']).order_by('-created_at')


class SingleNews(DetailView):
    model = News
    template_name = 'news/single-news.html'
    slug_url_kwarg = 'news_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = News.objects.select_related('author').get(slug=self.kwargs[self.slug_url_kwarg])
        context['title'] = news.title
        context['news'] = news
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

    # def get_object(self, queryset=None):
    #     return get_object_or_404(News, slug=self.kwargs[self.slug_url_kwarg])

    # def get_queryset(self):
    #     return News.objects.get(slug=self.kwargs[self.slug_url_kwarg])


class SingleTag(ListView):
    model = Tag
    context_object_name = 'news'
    template_name = 'news/index.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Tag: {Tag.objects.get(slug=self.kwargs["tag_slug"])}'
        return context

    def get_queryset(self):
        return News.objects.select_related('author', 'category').prefetch_related('tag')\
            .filter(tag__slug=self.kwargs['tag_slug'])


class AddNews(CreateView):
    form_class = AddNewsForm
    template_name = 'news/addpage.html'
    extra_context = {
        'title': 'Create News',
    }

    def form_valid(self, form):
        news = form.save(commit=False)
        news.author = self.request.user
        return super().form_valid(form)
