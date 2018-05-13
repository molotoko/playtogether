# -*- coding: utf-8 -*-

import requests
import re

from settings import steam_API_key as key

# For optimization purposes
# nickname_regexp = re.compile('^https?://steamcommunity.com/id/(.+)$', re.I)

profile_urls = ['http://steamcommunity.com/id/gwellir', 'http://steamcommunity.com/id/hwestar']

#for url in profile_urls:
def get_games(url):
    nickname = re.search('^https?://steamcommunity.com/id/(.+)$', url, re.I).group(1)
    steamID_result = requests.get('http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/', params = {'key': key, 'vanityurl': nickname})
    steamID = steamID_result.json()['response']['steamid']

    params = {'steamid': steamID, 'key': key, 'include_played_free_games': 1}
    result = requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/', params = params)
    games = result.json()['response']['games']
    game_ids = list(map(lambda game: game['appid'], games))

    return game_ids

profile_games = list(map(get_games, profile_urls))
print(profile_games)