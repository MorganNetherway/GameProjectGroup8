#import room file
from items import *
from minotaur import minotaur_movement_speed


player_stats = {"health": 100, "attack": 10, "defense": 10, "speed": 1}


#player's speed
#player_speed = 1

#player's health
#player_health = 100

#player's attack
#player_attack = 10

#player's defence
#player_defense = 10

#player's inventory
inventory = []

#player starts at ....
player_position = [7,0]

def update_stats_take(item):
    global minotaur_movement_speed
    global player_attack
    global player_defense
    global player_health
    global player_speed
    
    if "attack_value" in item:
        player_stats["attack"] *= item["attack_value"]
        return player_stats
    
    if "defense_value" in item:
        player_stats["defense"] *= item["defense_value"]
        return player_stats
    
    if "speed_value" in item:
        player_stats["speed"] *= item["speed_value"]
        return player_stats
    
    if "health_value" in item:
        player_health *= item["health_value"]
        return player_stats
    
    if "attack_boost" in item:
        player_stats["attack"] *= powerup_attack_boost["attack_boost"]
        return player_stats
    
    if "health_boost" in item:
        player_stats["health"] *= powerup_health_boost["health_boost"]
        return player_stats
    
    if "minotaur_speed_boost" in item:
        minotaur_movement_speed *= powerup_minotaur_half_speed["minotaur_speed_boost"]
        return player_stats

def update_stats_drop(item):
    global minotaur_movement_speed
    global player_attack
    global player_defense
    global player_health
    global player_speed

    if "attack_value" in item:
        player_stats["attack"] /= item["attack_value"]
        return player_stats
    
    if "defense_value" in item:
        player_stats["defense"]/= item["defense_value"]
        return player_stats
    
    if "speed_value" in item:
        player_stats["speed"] /= item["speed_value"]
        return player_stats
    
    if "health_value" in item:
        player_stats["health"] /= item["health_value"]
        return player_stats
    
    if "attack_boost" in item:
        player_stats["attack"] /= powerup_attack_boost["attack_boost"]
        return player_stats
    
    if "health_boost" in item:
        player_stats["health"] /= powerup_health_boost["health_boost"]
        return player_stats
    
    if "minotaur_speed_boost" in item:
        minotaur_movement_speed /= powerup_minotaur_half_speed["minotaur_speed_boost"]
        return player_stats
