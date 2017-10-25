import player
from minotaur import *
from movement import *
from word_translation import *
from drawMapFuncs import *
from minotaur_encounter import *
from rooms import *


turn = 0


availableExits = getAvailableExits(player_position)
minAvailableExits = getAvailableExits(minotaur_position)

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:
    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'
    >>> list_of_items([item_id])
    'id card'
    >>> list_of_items([])
    ''
    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'
    """
    csl_items = []

    for item in items:
        csl_items.append(item["name"])
    csl_list = ", ".join(csl_items)
    
    return csl_list

def moveOnMap(user_input):
    global player_position
    if user_input[1] == "north":
        if "north" in availableExits:
            if checkForTriggerGate(availableExits["north"]) == True:
                player_position = availableExits["north"]
        else:
            print ("You cannot go any further north")
    elif user_input[1] == "south":
        if "south" in availableExits:
            if checkForTriggerGate(availableExits["south"]) == True:
                player_position = availableExits["south"]
        else:
            print ("You cannot go any further south")
    elif user_input[1] == "west":
        if checkForTriggerGate(availableExits["west"]) == True:
            if "west" in availableExits:
                player_position = availableExits["west"]
        else:
            print ("You cannot go any further west")
    elif user_input[1] == "east":
        if checkForTriggerGate(availableExits["east"]) == True:
            if "east" in availableExits:
                player_position = availableExits["east"]
        else:
            print ("You cannot go any further east")
    else:
        print("That movement isn't possible, try again.")

def take_item(item_id):
    for i in range(0, len(current_room["items"])):
        if normalised_input[1] == current_room["items"][i]["id"]:
            print("taking", current_room["items"][i]["id"])
            item = current_room["items"].pop(i)
            inventory.append(item)
            update_stats_take(item)
            if "art" in item:
                print(item["art"])
            return
    else:
        print("You cannot take that")

def drop_item(item_id):
    for i in range(0, len(inventory)):
        if normalised_input[1] == inventory[i]["id"]:
            item = inventory.pop(i)
            current_room["items"].append(item)
            update_stats_drop(item)
            return
    else:
        print("You cannot drop that")

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:
    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>
    """
    item_length = len(items)
    item_list = []
    
    for x in range(0,item_length):

        if items[x]["id"] == "sword":
            item_list.append(item_sword)
        elif items[x]["id"] == "shield":
            item_list.append(item_shield)
        elif items[x]["id"] == "spear":
            item_list.append(item_spear)
        elif items[x]["id"] == "scroll_attack":
            item_list.append(item_scroll_attack)
        elif items[x]["id"] == "scroll_health":
            item_list.append(item_scroll_health)
        elif items[x]["id"] == "scroll_speed":
            item_list.append(item_scroll_speed)
        elif items[x]["id"] == "diary_1":
            item_list.append(item_diary_1)
        elif items[x]["id"] == "diary_2":
            item_list.append(item_diary_2)
        elif items[x]["id"] == "diary_3":
            item_list.append(item_diary_3)
        elif items[x]["id"] == "diary_4":
            item_list.append(item_diary_4)
        elif items[x]["id"] == "diary_5":
            item_list.append(item_diary_5)
        else:
            pass
    if len(item_list) == 0:
        pass
    else:
        x = list_of_items(item_list)
        print("You have " + x + ".")
print("")

while True:
    print(current_room)
    user_input = input("> ").lower()
    normalised_input = normalise_input(user_input)

    minotaurMove(minotaur_position)
    print(minotaur_position)

    if "go" in normalised_input:
        moveOnMap(normalised_input)

    elif "take" in normalised_input:
        if len(normalised_input) > 1:
            take_item(normalised_input[1])
        else:
            print("What do you want to take?")

    elif "drop" in normalised_input:
        if len(normalised_input) > 1:
            drop_item(normalised_input[1])
        else:
            print("What do you want to drop?")

    elif "inventory" in normalised_input:
        print_inventory_items(inventory)
        
            
    elif "show" in normalised_input:
        currentPosition = []
        position = convertToKey(player_position)
        currentPosition.append(position)
        
        board = movePlayerMap(currentPosition)
        showMap(board)

    else:
        print ("Please use the WASD keys to move")

    current_room = checkForTriggerRoom(player_position)
    availableExits = getAvailableExits(player_position)
    
    print("You are at " + convertToKey(player_position))
    if minotaur_position == player_position:
        encounter()
    turn += 1
