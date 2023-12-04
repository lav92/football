from django.urls import path
from stats.views import Home

app_name = 'stats'

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
