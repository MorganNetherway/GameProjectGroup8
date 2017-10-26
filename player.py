#imports the items so they be referenced from the player's inventory
from items import *

#creates a dictionary which contains various player stats, all used in the minotaur encounter
player_stats = {"health": 100, "attack": 10, "defense": 10}


#player's inventory, empty at the start but gets appended to when items are picked up,
#and items are popped out when dropped.
inventory = []

#player starting location - location 7,0 on the game grid
player_position = [7,0]

#defines a function which is called whenever the player picks up an item.
#it checks to see whether the item has a value modifier e.g. attack_value,
#and if it does, the value in the player_stats dictionary is updated.

def update_stats_take(item):

    #makes variables global so they can be updated in the fucntion without being returned
    global minotaur_movement_speed
    global player_attack
    global player_defense
    global player_health

    #checks to see whether the corresponding key is present on the taken item
    if "attack_value" in item:
        
        #multiplies the relevant stat by the item modifier
        player_stats["attack"] *= item["attack_value"]
        
        #returns the updated dictionary to the main loop
        return player_stats
    
    if "defense_value" in item:
        player_stats["defense"] *= item["defense_value"]
        return player_stats
    
    if "health_value" in item:
        player_stats["health"] *= item["health_value"]
        return player_stats
    
    if "attack_boost" in item:
        player_stats["attack"] *= powerup_attack_boost["attack_boost"]
        return player_stats
    
    if "health_boost" in item:
        player_stats["health"] *= powerup_health_boost["health_boost"]
        return player_stats

#defines a function which is called whenever the player drops an item.
#it checks to see whether the item has a value modifier e.g. attack_value,
#and if it does, the value in the player_stats dictionary is updated.
    
def update_stats_drop(item):
    
    #makes variables global so they can be updated in the fucntion without being returned
    global minotaur_movement_speed
    global player_attack
    global player_defense
    global player_health
    
    #checks to see whether the corresponding key is present on the taken item
    if "attack_value" in item:
        
        #divides the relevant stat by the item modifier
        player_stats["attack"] /= item["attack_value"]
        
        #returns the updated dictionary to the main loop
        return player_stats
    
    if "defense_value" in item:
        player_stats["defense"]/= item["defense_value"]
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
