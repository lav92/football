import requests
from datetime import *
import calendar

# uri_table = 'https://api.football-data.org/v4/competitions/PL/standings'
# headers = {'X-Auth-Token': '58e6cb6d63de4b5fa5e98defa3b17d3d'}
#
# response_table = requests.get(uri_table, headers=headers)
# print(type(response_table.json()))
# teams_dict = list()
#
#
# def get_table():
#     result = list()
#     for k, v in response_table.json().items():
#         if k == 'standings':
#             for key, value in v[0].items():
#                 if key == 'table':
#                     for pos in value:
#                         result.append(pos)
#     return result
#
#
# for item in get_table():
#     print(item)

# print('---------')
# uri_matches = 'https://api.football-data.org/v4/competitions/PL/matches?matchday=14'
# response_matchday = requests.get(uri_matches, headers=headers)
# for k, v in response_matchday.json().items():
#     print(k, v)
#     if isinstance(v, list):
#         for num, item in enumerate(v):
#             print(num, item)

# uri_scores = 'https://api.football-data.org/v4/competitions/PL/standings'
uri_scores = 'https://api.football-data.org/v4/competitions/PL/matches'
headers = {'X-Auth-Token': '58e6cb6d63de4b5fa5e98defa3b17d3d'}

response = requests.get(uri_scores, headers=headers)

matches_played = response.json().get('resultSet').get('played')
print(matches_played, type(matches_played))

# start = datetime(2023, 12, 4)
# finish = datetime(2023, 11, 7)
# print(datetime.now())
# print(datetime.now() > start)

