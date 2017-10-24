from player import *
from movement import *
from word_translation import *
from minotaur_encounter import *

current_room = {"items": [item_sword, item_spear]}

availableExits = getAvailableExits(player_position)
minAvailableExits = getAvailableExits(minantour_position)

def moveOnMap(user_input):
    global player_position
    if user_input == "w":
        if "north" in availableExits:
            player_position = availableExits["north"]
        else:
            print ("You cannot go any further north")
    elif user_input == "s":
        if "south" in availableExits:
            player_position = availableExits["south"]
        else:
            print ("You cannot go any further south")
    elif user_input == "a":
        if "west" in availableExits:
            player_position = availableExits["west"]
        else:
            print ("You cannot go any further west")
    elif user_input == "d":
        if "east" in availableExits:
            player_position = availableExits["east"]
        else:
            print ("You cannot go any further east")

def take_item(item_id):
    for i in range(0, len(current_room["items"])):
        if normalised_input[1] == current_room["items"][i]["id"]:
            item = current_room["items"].pop(i)
            inventory.append(item)
            update_stats(item)
            return
        else:
            print("You cannot take that")

def drop_item(item_id):
    for i in range(0, len(inventory)):
        if normalised_input[1] == inventory[i]["id"]:
            current_room["items"].append(inventory.pop(i))
        else:
            print("You cannot drop that")
    
while True:
    user_input = input("W/A/S/D > ").lower()
    normalised_input = normalise_input(user_input)
    if user_input in "wasd":
        moveOnMap(user_input)
        
    elif "take" in normalised_input:
        if len(normalised_input) > 1:
            take_item(normalised_input[1])
            
        else:
            print("What do you want to take?")
            
    elif "drop" in user_input:
        if len(normalised_input) > 1:
            drop_item(normalised_input[1])
        else:
            print("What do you want to drop?")
    else:
        print ("Please use the WASD keys to move")
    checkForTriggerRoom(player_position)
    availableExits = getAvailableExits(player_position)
    print("You are at " + convertToKey(player_position))    
    
