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

#turn is used as a score at the end
#could also be used as part of functionality in future
#eg speed boost
turn = 0

#get all possible next moves for player and minotaur
availableExits = getAvailableExits(player_position)
minAvailableExits = getAvailableExits(minotaur_position)

#function to turn a list into a csv string
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

#takes in item_id and uses it to add item to inventory
def take_item(item_id):
    #cant pick up items when not in a room
    if current_room == None:
        print("There is nothing here.")
        return
    else:
        #iterate through all items in current room
        for i in range(0, len(rooms[current_room]["items"])):
            #if the item you wanted to take matches with an item in the room
            #remove item from room items
            #add to player inventory
            #update stats if item affects stats
            if normalised_input[1] == rooms[current_room]["items"][i]["id"]:
                print("Taking", rooms[current_room]["items"][i]["id"])
                item = rooms[current_room]["items"].pop(i)
                inventory.append(item)
                update_stats_take(item)
                #if item has associated ascii art
                #print art
                if "art" in item:
                    print(item["art"])
                return
        else:
            print("You cannot take that")

def drop_item(item_id):
    for i in range(0, len(inventory)):
        if normalised_input[1] == inventory[i]["id"]:
            #cannot drop items outside of a room
            if current_room == None:
                print()
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
        print(item_diary_2["description"])
    if diary == "diary_3":
        print(item_diary_3["description"])
    if diary == "diary_4":
        print(item_diary_4["description"])
    if diary == "diary_5":
        print(item_diary_5["description"])
    pass

def print_inventory_items(items):
    item_length = len(items)
    item_list = []

    if inventory == []:
        print("You have nothing haha!")
    else:
        for item in inventory:
            item_list.append(item["name"])
        print("You have " + ", ".join(item_list))
        
#main game loop
while True:
    user_input = input("> ").lower()
    normalised_input = normalise_input(user_input)


    if "go" in normalised_input:
        if moveOnMap(normalised_input):
            #code to move minotaur
            minotaur_position = minotaurMove(minotaur_position, minAvailableExits)
            #gets distance between you and minotaur and if it within 1 then alert user
            if math.sqrt((minotaur_position[0] - player_position[0])**2 + (minotaur_position[1] - player_position[1])**2) < 3:
                print()
                print ("The minatour is close.")
            print("Minatour Position: {}".format(minotaur_position))
    elif "take" in normalised_input:
        if len(normalised_input) > 1:
            take_item(normalised_input[1])
        else:
            print()
            print("What do you want to take?")

    elif "drop" in normalised_input:
        if len(normalised_input) > 1:
            drop_item(normalised_input[1])
        else:
            print()
            print("What do you want to drop?")

    elif "inventory" in normalised_input:
        print_inventory_items(inventory)

    #this calls the functions to update and print the map
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
    #check to see if youve entered a room when you move
    current_room = checkForTriggerRoom(player_position)

    availableExits = getAvailableExits(player_position)
    minAvailableExits = getAvailableExits(minotaur_position)
    print("You are at " + convertToKey(player_position))

    #calls function that deals with minotaur battle
    if minotaur_position == player_position:
        encounter(player_position)

    #winning/losin/drawing conditions
    if player_stats["health"] <= 0:
        print()
        print('''After a grueling spar with the minotaur, you have followed in the footsteps of Theseus, and have fallen before the Minotaur.''')
        break

    if minotaur_stats["health"] <= 0:
        print()
        print('''The tremendous roars of the minotaur stops. Your heart begins beating softer and slower, the only adrenaline remaining coming from the knowledge that, finally the Minotaur has fallen.''')
        print()
        print("You took " + str(turn) + " turns to beat the game.")
        break
    #increase turn at end of loop
    turn += 1
