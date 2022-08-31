import requests
import mcuuid

def get_stats(name, mode):
    api_key = "b1965d7b-5381-470e-9e0e-7417aceaed4c"
    player = mcuuid.MCUUID(name=name)
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

    return [bedwars_wins, bedwars_losses, bedwars_finals, bedwars_final_deaths, bedwars_fkdr, bedwars_wlr, bedwars_star, bedwars_winstreak]


# def compare_format(player_one_data):

def compare(name, mode):
    counter = 0

    for i in name:
        if counter == 0:
            player_one_data = get_stats(i, mode)
            player1 = name[0]

        else:
            player_two_data = get_stats(i, mode)
            player2 = name[1]
            continue

        counter = counter + 1
# wins

    if player_one_data[0] > player_two_data[0]:
        print("{} has {} more wins than {}".format(player1, player_one_data[0] - player_two_data[0], player2))

    elif player_two_data[0] > player_one_data[0]:
        print("{} has {} more wins than {}".format(player2, player_two_data[0] - player_one_data[0], player1))

    else:
        print("both players have the same amount of wins")


    # losses

    if player_one_data[1] > player_two_data[1]:
        print("{} has {} more losses than {}".format(player1, player_one_data[1] - player_two_data[1], player2))

    elif player_two_data[1] > player_one_data[1]:
        print("{} has {} more losses than {}".format(player2, player_two_data[1] - player_one_data[1], player1))

    else:
        print("both players have the same amount of losses")

    # finals

    if player_one_data[2] > player_two_data[2]:
        print("{} has {} more finals than {}".format(player1, player_one_data[2] - player_two_data[2], player2))

    elif player_two_data[2] > player_one_data[2]:
        print("{} has {} more finals than {}".format(player2, player_two_data[2] - player_one_data[2], player1))

    else:
        print("both players have the same amount of finals")
# final deaths

    if player_one_data[3] > player_two_data[3]:
        print("{} has {} more final deaths than {}".format(player1, player_one_data[3] - player_two_data[3], player2))

    elif player_two_data[3] > player_one_data[3]:
        print("{} has {} more final deaths than {}".format(player2, player_two_data[3] - player_one_data[3], player1))

    else:
        print("both players have the same amount of final deaths")

        # fkdr

    if player_one_data[4] > player_two_data[4]:
        print("{} has {} higher fkdr than {}".format(player1, player_one_data[4] - player_two_data[4], player2))

    elif player_two_data[4] > player_one_data[4]:
        print("{} has {} higher fkdr than {}".format(player2, player_two_data[4] - player_one_data[4], player1))

    else:
        print("both players have the same fkdr")

    # wlr

    if player_one_data[5] > player_two_data[5]:
        print("{} has {} higher wlr than {}".format(player1, player_one_data[5] - player_two_data[5], player2))

    elif player_two_data[5] > player_one_data[5]:
        print("{} has {} higher wlr than {}".format(player2, player_two_data[5] - player_one_data[5], player1))

    else:
        print("both players have the same wlr")

    # star

    if player_one_data[6] > player_two_data[6]:
        print("{} has {} higher star than {}".format(player1, player_one_data[6] - player_two_data[6], player2))

    elif player_two_data[6] > player_one_data[6]:
        print("{} has {} higher star than {}".format(player2, player_two_data[6] - player_one_data[6], player1))

    else:
        print("both players have the same star level")
# winstreak

    if player_one_data[7] > player_two_data[7]:
        print("{} has {} higher winstreak than {}".format(player1, player_one_data[7] - player_two_data[7], player2))

    elif player_two_data[7] > player_one_data[7]:
        print("{} has {} higher winstreak than {}".format(player2, player_two_data[7] - player_one_data[7], player1))

    else:
        print("both players have the same winstreak")



compare_or_view = input("would you like to compare or view players stats? ").lower()

if compare_or_view == "compare":
    player_names = input("Enter two names to compare").lower()
    player_names_list = player_names.rsplit(" ")

    if len(player_names_list) == 2:
        mode_name = "eight_two_"
        compare(player_names_list, mode_name)


    else:
        print("two names were not inputed")

elif compare_or_view == "view":

    name = input("Enter a Player name: ")
    name_list = name.rsplit(" ")
    mode = input("Enter mode: ").upper()

    if mode == "SOLOS":
        mode_name = "eightone"
    elif mode == "DUOS":
        mode_name = "eighttwo"
    elif mode == "THREES":
        mode_name = "fourthree"
    elif mode == "FOURS":
        mode_name = "fourfour"
    elif mode == "4v4":
        mode_name = "twofour"
    else:
        print("You didn't input a mode, so we are printing your overall stats!!")
        mode_name = ""

    for i in name_list:
        bedwars_data = get_stats(name, mode_name)

        print("Wins: {} "
              "Losses: {} "
              "Finals: {} "
              "Final deaths: {} "
              "FKDR: {} "
              "WLR: {} "
              "Star: {} "
              "Winstreak: {} ".format(bedwars_data[0], bedwars_data[1], bedwars_data[2], bedwars_data[3], bedwars_data[4], bedwars_data[5], bedwars_data[6], bedwars_data[7]))