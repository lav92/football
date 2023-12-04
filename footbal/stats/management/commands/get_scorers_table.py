from django.core.management import BaseCommand
from stats.models import Player, TableScorers
from stats.api_requests import get_scorers
from django.db.utils import IntegrityError


class Command(BaseCommand):
    def handle(self, *args, **options):
        TableScorers.objects.all().delete()
        self.stdout.write('Заполним таблицу бомбардиров')
        for row in get_scorers():
            TableScorers.objects.update_or_create(players=Player.objects.get(name=row.get('player').get('name')),
                                                  goals=row.get('goals'),
                                                  assists=row.get('assists') if row.get('assists') is not None else 0)
        self.stdout.write('готово')
1