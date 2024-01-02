from django.urls import path, include
from django.views.decorators.cache import cache_page


from news.views import HomePage, SingleCategory, SingleNews, SingleTag
from news.api_views import AllNewsAPI, AllCategoryAPI, NewsByCategory, GetUpdateDeleteNewsAPI, CreateNewsAPI

urlpatterns = [
    path('', HomePage.as_view(), name='main-page'),
    path('category/<slug:cat_slug>/', SingleCategory.as_view(), name='category'),
    path('news/<slug:news_slug>/', cache_page(60 * 2)(SingleNews.as_view()), name='single'),
    path('tag/<slug:tag_slug>/', SingleTag.as_view(), name='tag'),
    # api urls for guest users
    path('api/v1/all_news/', AllNewsAPI.as_view()),
    path('api/v1/all_category/', AllCategoryAPI.as_view()),
    path('api/v1/news_by_category/<int:cat_pk>/', NewsByCategory.as_view()),

    path('api/v1/create_news/', CreateNewsAPI.as_view()),
    path('api/v1/get_update_delete_news/<int:pk>/', GetUpdateDeleteNewsAPI.as_view()),
]
