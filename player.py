#from items import *
#import room file

#players health - can be used globally to be modified by items/scrolls
player_health = 100

#players attack - can be used globally to be modified by items/scrolls
player_attack = 10

#players defence - can be used globally to be modified by items/scrolls
player_defense = 10

#player's inventory
inventory = []

#player starts at ....
player_position = [7,0]

def equip_item():
    global player_attack
    global player_defense
    for item in inventory:
        if "attack_value" in item:
            player_attack *= item["attack_value"]
        if "defense_value" in item:
            player_defense *= item["defense_value"]
