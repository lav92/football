from django.urls import path, include

from news.views import HomePage, single_news

urlpatterns = [
    path('', HomePage.as_view(), name='main-page'),
    path('news/<slug:news_slug>/', single_news, name='single')
]
