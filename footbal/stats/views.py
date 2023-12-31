from django.views.generic import ListView
import requests
from django.core import management
from django.core.cache import cache

from stats.models import Table, TableScorers


class Home(ListView):
    model = Table
    template_name = 'stats/home.html'
    context_object_name = 'table_teams'
    extra_context = {
        'title': 'Stats',
        'table_scorers': TableScorers.objects.select_related('players__team').prefetch_related().all(),
    }

    def get_queryset(self):
        link = 'https://api.football-data.org/v4/competitions/PL/matches'
        headers = {'X-Auth-Token': '58e6cb6d63de4b5fa5e98defa3b17d3d'}
        result = cache.get('table')
        if not result:
            response = requests.get(link, headers=headers)
            matches_played = response.json().get('resultSet').get('played')
            print(matches_played)
            if matches_played % 10 != 0:
                management.call_command('get_table')
            result = Table.objects.select_related('team').all()
            cache.set('table', result, 60*3)
        return result
