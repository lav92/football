from django.urls import path, include

from news.views import HomePage, SingleCategory, SingleNews, SingleTag, AddNews

urlpatterns = [
    path('', HomePage.as_view(), name='main-page'),
    path('category/<slug:cat_slug>/', SingleCategory.as_view(), name='category'),
    path('news/<slug:news_slug>/', SingleNews.as_view(), name='single'),
    path('tag/<slug:tag_slug>/', SingleTag.as_view(), name='tag'),
]
