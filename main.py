from player import *
from movement import *


availableExits = getAvailableExits(player_position)
minAvailableExits = getAvailableExits(minPos)

while True:
    user_input = input("W/A/S/D > ").lower()
    if user_input in "wasd":
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
    else:
        print ("Please use the WASD keys to move")
    checkForTriggerRoom(player_position)
    availableExits = getAvailableExits(player_position)
    print("You are at " + convertToKey(player_position))
