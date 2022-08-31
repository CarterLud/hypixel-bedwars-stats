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


def get_stats(name, mode):
    for i in name:
        api_key = "d7a794fb-1e52-422d-85af-f19ad1c70a9e"
        player = mcuuid.MCUUID(name=i)
        uuid = player.uuid
        uri = "https://api.hypixel.net/player?key={}&uuid={}"
        url = uri.format(api_key, uuid)
        response = requests.get(url).json()

        bedwars_wins = response.get('player').get('stats').get('Bedwars').get(mode + 'wins_bedwars')
        bedwars_losses = response.get('player').get('stats').get('Bedwars').get(mode + 'losses_bedwars')
        bedwars_finals = response.get('player').get('stats').get('Bedwars').get(mode + 'final_kills_bedwars')
        bedwars_final_deaths = response.get('player').get('stats').get('Bedwars').get(mode + 'final_deaths_bedwars')
        bedwars_fkdr = round((bedwars_finals / bedwars_final_deaths), 3)
        bedwars_wlr = round((bedwars_wins / bedwars_losses), 3)
        bedwars_winstreak = response.get('player').get('stats').get('Bedwars').get(mode + 'winstreak')
        bedwars_star = response.get('player').get('achievements').get("bedwars_level")
        print("Name: {} "
              "Wins: {} "
              "Losses: {} "
              "Finals: {} "
              "Final deaths: {} "
              "FKDR: {} "
              "WLR: {} "
              "Star: {} "
              "Winstreak: {} ".format(i, bedwars_wins, bedwars_losses, bedwars_finals, bedwars_final_deaths,
                                      bedwars_fkdr, bedwars_wlr, bedwars_star, bedwars_winstreak)
              )


while True:
    print("\n")
    name = input("Enter player name (if mulitple seperate by spaces): ")
    name_list = name.rsplit(" ")
    mode = input("Enter mode: ").upper()

    if mode == "SOLOS":
        mode_name = "eight_one_"
    elif mode == "DUOS":
        mode_name = "eight_two_"
    elif mode == "THREES":
        mode_name = "four_three_"
    elif mode == "FOURS":
        mode_name = "four_four_"
    elif mode == "4v4":
        mode_name = "two_four_"
    else:
        print("You didn't input a mode, so we are printing your overall stats!!")
        mode_name = ""

    get_stats(name_list, mode_name)

