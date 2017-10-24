#import room file
from items import *
from powerups import *
from minotaur import minotaur_movement_speed

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
    global minotaur_movement_speed
    global player_attack
    global player_defense
    global player_health

    for item in inventory:
        if "attack_value" in item:
            player_attack *= item["attack_value"]
        if "defense_value" in item:
            player_defense *= item["defense_value"]
        if "attack_boost" in item:
            player_attack *= powerup_attack_boost["attack_boost"]
        if "health_boost" in item:
            player_health *= powerup_health_boost["health_boost"]
        if "speed_boost" in item:
            minotaur_movement_speed *= powerup_minotaur_half_speed["speed_boost"]

    return
