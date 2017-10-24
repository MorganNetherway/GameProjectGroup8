#import room file
from items import *
from powerups import *
from minotaur import minotaur_movement_speed

#player's speed
player_speed = 1

#player's health
player_health = 100

#player's attack
player_attack = 10

#player's defence
player_defense = 10

#player's inventory
inventory = [item_sword, item_shield, item_scroll_attack, item_scroll_health, item_scroll_speed, powerup_attack_boost, powerup_health_boost, powerup_minotaur_half_speed]

#player starts at ....
player_position = [7,0]
minantour_position = [6,7]

def update_stats():
    global minotaur_movement_speed
    global player_attack
    global player_defense
    global player_health
    global player_speed

    for item in inventory:
        if "attack_value" in item:
            player_attack *= item["attack_value"]
        if "defense_value" in item:
            player_defense *= item["defense_value"]
        if "speed_value" in item:
            player_speed *= item["speed_value"]
        if "health_value" in item:
            player_health *= item["health_value"]
        if "attack_boost" in item:
            player_attack *= powerup_attack_boost["attack_boost"]
        if "health_boost" in item:
            player_health *= powerup_health_boost["health_boost"]
        if "minotaur_speed_boost" in item:
            minotaur_movement_speed *= powerup_minotaur_half_speed["minotaur_speed_boost"]

    return
