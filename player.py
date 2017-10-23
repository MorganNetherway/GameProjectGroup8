#from items import *
#import room file

#players health
player_health = 100

#players attack
player_attack = 10

#players defence
player_defense = 10

#player's inventory
inventory = []

#player starts at ....
player_position = [7,0]
minantour_position = [6,7]

def update_stats():
    global player_attack
    global player_defense

    for item in inventory:
        if "attack_value" in item:
            player_attack *= item["attack_value"]
        if "defense_value" in item:
            player_defense *= item["defense_value"]

    if powerup_attack_boost in inventory:
        player_attack *=

    if powerup_health_boost in inventory:
        player_attack *=

    if powerup_minotaur_half_speed in inventory:
