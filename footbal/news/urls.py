from django.urls import path, include
from django.views.decorators.cache import cache_page


from news.views import HomePage, SingleCategory, SingleNews, SingleTag, video, NewsAPI

urlpatterns = [
    path('', HomePage.as_view(), name='main-page'),
    path('category/<slug:cat_slug>/', SingleCategory.as_view(), name='category'),
    path('news/<slug:news_slug>/', cache_page(60 * 2)(SingleNews.as_view()), name='single'),
    path('tag/<slug:tag_slug>/', SingleTag.as_view(), name='tag'),
    path('videos/', video, name='video'),
    path('api/v1/newsall/', NewsAPI.as_view()),
]
