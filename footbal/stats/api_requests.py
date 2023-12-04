import requests

headers = {'X-Auth-Token': '58e6cb6d63de4b5fa5e98defa3b17d3d'}


def get_teams():
    teams_list = list()
    response = requests.get('https://api.football-data.org/v4/competitions/PL/standings', headers=headers)
    for item in response.json().get('standings')[0].get('table'):
        teams_list.append(item.get('team'))

    return teams_list


def get_table():
    response = requests.get('https://api.football-data.org/v4/competitions/PL/standings', headers=headers)
    return response.json().get('standings')[0].get('table')


def get_scorers():
    response = requests.get('https://api.football-data.org/v4/competitions/PL/scorers', headers=headers)
    return response.json().get('scorers')
