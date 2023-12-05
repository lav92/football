from django.urls import path
from stats.views import Home
from django.views.decorators.cache import cache_page


app_name = 'stats'

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
