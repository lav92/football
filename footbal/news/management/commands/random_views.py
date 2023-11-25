from django.core.management import BaseCommand
from random import randint
from news.models import News


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('присвоим рандомное количество просмотров всем новостям')
        for item in News.objects.all():
            item.views = randint(1, 1000)
            item.save()
        self.stdout.write('Done')