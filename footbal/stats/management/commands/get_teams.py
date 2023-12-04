from django.core.management import BaseCommand
from stats.models import Team
from stats.api_requests import get_teams
from django.db.utils import IntegrityError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Заполним таблицу комадами участниками АПЛ')
        for team in get_teams():
            try:
                Team.objects.create(fullname=team.get('name'), name=team.get('shortName'), tla=team.get('tla'),
                                    logo=team.get('crest'), data_football_id=team.get('id'))
                self.stdout.write(f'Создана команда {team.get("name")}')
            except IntegrityError:
                print('имя команды должны быть уникальным')
        self.stdout.write('готово')
