from django.core.management import BaseCommand
from stats.models import Player, Team
from stats.api_requests import get_scorers
from django.db.utils import IntegrityError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Заполним таблицу игроков бомбардиров')
        for item in get_scorers():
            Player.objects.create(name=item.get('player').get('name'), first_name=item.get('player').get('firstName'),
                                  last_name=item.get('player').get('lastName'),
                                  nationality=item.get('player').get('nationality'),
                                  section=item.get('player').get('section'),
                                  data_football_id=item.get('player').get('id'),
                                  team=Team.objects.get(name=item.get('team').get('shortName')))
        self.stdout.write('готово')
