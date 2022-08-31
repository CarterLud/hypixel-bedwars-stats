import math

import requests
import mcuuid
import pprint

from os import path


key_path = 'key.txt'


def get_key():
    if not path.exists(key_path):
        key_input = input("Please enter your Hypixel API Key: ").strip()
        save_key(key_input)
        return key_input

    with open(key_path, 'r') as key_file:
        key = key_file.read().strip()
    return key


def save_key(new_key):
    with open(key_path, 'w') as key_file:
        key_file.write(new_key)


def get_duos_stats(name):
    api_key = get_key()
    player = mcuuid.MCUUID(name=name)
    uuid = player.uuid
    uri = "https://api.hypixel.net/player?key={}&uuid={}"
    url = uri.format(api_key, uuid)
    response = requests.get(url).json()

    bedwars_duos_final_deaths = response.get('player').get('stats').get('Bedwars').get('eight_two_final_deaths_bedwars')
    bedwars_duos_losses = response.get('player').get('stats').get('Bedwars').get('eight_two_losses_bedwars')
    bedwars_level = response.get('player').get('achievements').get('bedwars_level')
    bedwars_duos_wins = response.get('player').get('stats').get('Bedwars').get('eight_two_wins_bedwars')
    bedwars_duos_finals = response.get('player').get('stats').get('Bedwars').get('eight_two_final_kills_bedwars')
    bedwars_duos_final_deaths = response.get('player').get('stats').get('Bedwars').get('eight_two_final_deaths_bedwars')
    bedwars_finals = response.get('player').get('stats').get('Bedwars').get('final_kills_bedwars')
    bedwars_final_deaths = response.get('player').get('stats').get('Bedwars').get('final_deaths_bedwars')
    bedwars_duos_fkdr = round((bedwars_duos_finals / bedwars_duos_final_deaths), 3)
    bedwars_fkdr = round((bedwars_finals / bedwars_final_deaths), 3)
    bedwars_duos_wlr = round((bedwars_duos_wins / bedwars_duos_losses), 3)
    print("This person has: {} bedwars duos finals, {} bedwars duos final deaths and {} bedwars duos wins.".format(bedwars_duos_finals, bedwars_duos_wins, bedwars_duos_final_deaths))
    print("This person's overall FKDR is {}.".format(bedwars_fkdr))
    print("This person's duos FKDR is {}".format(bedwars_duos_fkdr))
    print("This person's duos WLR is {}".format(bedwars_duos_wlr))
    print("This person has {} stars.".format(bedwars_level))


while True:
    name = input("Enter a player name for duos stats: ")
    get_duos_stats(name)


def get_4v4_stats(name):
    api_key = get_key()
    player = mcuuid.MCUUID(name=name)
    uuid = player.uuid
    uri = "https://api.hypixel.net/player?key={}&uuid={}"
    url = uri.format(api_key, uuid)
    response = requests.get(url).json()

    bedwars_4v4_wins = response.get('player').get('stats').get('Bedwars').get('two_four_wins_bedwars')
    bedwars_4v4_losses = response.get('player').get('stats').get('Bedwars').get('two_four_losses_bedwars')
    bedwars_4v4_finals = response.get('player').get('stats').get('Bedwars').get('two_four_final_kills_bedwars')
    bedwars_4v4_final_deaths = response.get('player').get('stats').get('Bedwars').get('two_four_final_deaths_bedwars')
    bedwars_4v4_fkdr = round((bedwars_4v4_finals / bedwars_4v4_final_deaths), 3)
    bedwars_4v4_wlr = round((bedwars_4v4_wins / bedwars_4v4_losses), 3)
    print("This person's 4v4 FKDR is {}".format(bedwars_4v4_fkdr))
    print("This person's 4v4 WLR is {}".format(bedwars_4v4_wlr))


while True:
    name = input("Enter a player name for 4v4 stats: ")
    get_4v4_stats(name)
