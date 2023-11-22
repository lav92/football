from django.shortcuts import render

from news.models import News


def main_page(request):
    data = {
        'title': 'Main Page',
        'news': News.objects.all(),
    }
    return render(request, 'news/index.html', context=data)
