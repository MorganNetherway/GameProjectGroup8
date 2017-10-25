import player
from minotaur import *
from movement import *
from word_translation import *
from drawMapFuncs import *
from minotaur_encounter import *
from rooms import *
import math
from items import *
from initialise import *

turn = 0

availableExits = getAvailableExits(player_position)
minAvailableExits = getAvailableExits(minotaur_position)

def list_of_items(items):
    l_items = []

    for item in items:
        l_items.append(item["name"])
    l_list = ", ".join(l_items)

    return l_list

def moveOnMap(user_input):
    global player_position

    if user_input[1] == "north":
        if "north" in availableExits:
            if checkForTriggerGate(availableExits["north"], player.inventory) == True:
                player_position = availableExits["north"]
                return True
        else:
            print ("You cannot go any further north")
    elif user_input[1] == "south":
        if "south" in availableExits:
            if checkForTriggerGate(availableExits["south"], player.inventory) == True:
                player_position = availableExits["south"]
                return True
        else:
            print ("You cannot go any further south")
    elif user_input[1] == "west":
        if "west" in availableExits:
            if checkForTriggerGate(availableExits["west"], player.inventory) == True:
                player_position = availableExits["west"]
                return True
        else:
            print ("You cannot go any further west")
    elif user_input[1] == "east":
        if "east" in availableExits:
            if checkForTriggerGate(availableExits["east"], player.inventory) == True:
                player_position = availableExits["east"]
                return True
        else:
            print ("You cannot go any further east")
    else:
        print("That movement isn't possible, try again.")

def take_item(item_id):
    if current_room == None:
        print("There is nothing here.")
        return
    else:
        for i in range(0, len(rooms[current_room]["items"])):
            if normalised_input[1] == rooms[current_room]["items"][i]["id"]:
                print("taking", rooms[current_room]["items"][i]["id"])
                item = rooms[current_room]["items"].pop(i)
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
            if current_room == None:
                print("You cannot drop that.")
            else:
                item = inventory.pop(i)
                rooms[current_room]["items"].append(item)
                update_stats_drop(item)
                return
        else:
            print("You cannot drop that.")

def read_item(diary):
    if diary == "diary_1":
        print(item_diary_1["description"])
    if diary == "diary_2":
        print(item_diary_1["description"])
    if diary == "diary_3":
        print(item_diary_1["description"])
    if diary == "diary_4":
        print(item_diary_1["description"])
    if diary == "diary_5":
        print(item_diary_1["description"])
    pass

def print_inventory_items(items):
    item_length = len(items)
    item_list = []

    for x in range(0,item_length):
        item_list.append(item_refs[items[x]["id"]])
        
    if len(item_list) == 0:
        print("You have nothing haha")
    else:
        x = list_of_items(item_list)
        print("You have " + x + ".")
print("")

while True:
    user_input = input("> ").lower()
    normalised_input = normalise_input(user_input)


    if "go" in normalised_input:
        if moveOnMap(normalised_input):
            minotaur_position = minotaurMove(minotaur_position, minAvailableExits)
            if math.sqrt((minotaur_position[0] - player_position[0])**2 + (minotaur_position[1] - player_position[1])**2) < 3:
                print ("The minatour is close.")
            print("Minatour Position: {}".format(minotaur_position))
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

    elif "read" in normalised_input:
        if len(normalised_input) > 1:
            read_item(normalised_input[1])
            
        else:
            print("What do you want to read?")

    else:
        print ("Please enter a valid command. Hint: try 'go', 'read', 'take', 'show' or 'inventory'")

    current_room = checkForTriggerRoom(player_position)
    availableExits = getAvailableExits(player_position)
    minAvailableExits = getAvailableExits(minotaur_position)
    print("You are at " + convertToKey(player_position))
    if minotaur_position == player_position:
        encounter()

    if player_stats["health"] <= 0:
        print('''After a grueling spar with the minotaur, you have followed in the footsteps of Theseus, and have fallen before the Minotaur.''')
        break

    if minotaur_health <= 0:
        print('''The tremendous roars of the minotaur stops. You heart begins beating softer and slower, the only adrenaline remaining coming from the knwoelege that, finally the Minotaur has fallen.''')
        break

    if minotaur_health and player_stats["health"] <= 0:
        print('''Looking at your broken body splayed across the floor, you achknowlege that you will soon be following Theseus into the afterlife. But, before you take your last breathe, you look across the room and realise you have accomplished that which he could not: killed the Minotaur.''')
        break

    turn += 1
