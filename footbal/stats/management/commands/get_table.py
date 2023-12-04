from django.core.management import BaseCommand
from stats.models import Team, Table
from stats.api_requests import get_table
from django.db.utils import IntegrityError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Заполним таблицу комадами участниками АПЛ')
        Table.objects.all().delete()
        for item in get_table():
            Table.objects.create(position=item['position'], team=Team.objects.get(name=item.get('team').get('shortName')),
                                 played_games=item['playedGames'], won=item['won'], draw=item['draw'],
                                 lost=item['lost'], points=item['points'], goals_for=item['goalsFor'],
                                 goals_against=item['goalsAgainst'], goal_difference=item['goalDifference'])
        self.stdout.write('готово')
