import requests

headers = {'X-Auth-Token': '58e6cb6d63de4b5fa5e98defa3b17d3d'}


def get_teams():
    teams_list = list()
    response = requests.get('https://api.football-data.org/v4/competitions/PL/standings', headers=headers)
    for k, v in response.json().items():
        if k == 'standings':
            for key, value in v[0].items():
                if key == 'table':
                    for pos in value:
                        for row, column in pos.items():
                            if row == 'team':
                                teams_list.append(column)

    return teams_list


def get_table():
    result = list()
    response = requests.get('https://api.football-data.org/v4/competitions/PL/standings', headers=headers)
    for k, v in response.json().items():
        if k == 'standings':
            for key, value in v[0].items():
                if key == 'table':
                    for pos in value:
                        result.append(pos)
    return result


def get_scorers():
    result = list()
    response = requests.get('https://api.football-data.org/v4/competitions/PL/scorers', headers=headers)
    for key, value in response.json().items():
        if key == 'scorers':
            for item in value:
                result.append(item)
    return result
