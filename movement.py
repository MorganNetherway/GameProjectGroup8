import random
from player import *
from rooms import *
from riddles import *

#sets the current room to None at the start of the game, as the player
#does not start in a room
current_room = None

#creates a list of all the grid locations that the player cannot go,
#namely walls and the level boundaries
blockedExits = [
    "0,14", "0,13", "0,12", "0,11",
    "1,14", "1,12", "1,11", "1,9", "1,5", "1,3", "1,1",
    "2,14", "2,9", "2,7", "2,5", "2,4", "2,3", "2,2", "2,1",
    "3,14", "3,12", "3,11", "3,9", "3,5", "3,2", "3,1",
    "4,14", "4,12", "4,11", "4,9", "4,8", "4,6", "4,5",
    "5,14", "5,12", "5,11", "5,9", "5,5", "5,4", "5,3", "5,2", "5,0",
    "6,5", "6,2", "6,0",
    "7,11","7,9", "7,5", "7,4", "7,2",
    "8,14", "8,12", "8,11", "8,10", "8,9", "8,8", "8,6", "8,5", "8,2", "8,0",
    "9,11", "9,6", "9,5", "9,4", "9,0",
    "10,13", "10,11", "10,9", "10,8", "10,7", "10,6", "10,5", "10,4", "10,2", "10,1", "10,0",
    "11,11", "11,9", "11,8", "11,7","11,6","11,5", "11,4", "11,2", "11,1", "11,0",
    "12,13", "12,12", "12,11","12,5", "12,1",
    "13,13", "13,12", "13,9", "13,8",
    "14,9", "14,8", "14,7", "14,6", "14,5", "14,1"
]

#creates a list with the grid locations of all the gates - locations which the
#player must either answer a riddle or posses the correct key
gates = ["0,3", "4,2","4,10","8,7", "4,7", "6,9","13,1","13,5"]


#creates a list of dictionaries for each of the trigger points,
#which are grid locations where the current room will be updated.
#each dictionary contains the grid coordinates and the room name
#(corresponding to rooms.py)
triggerRooms = [
    {"positions": ["2,7"], "roomName": "special_well"},
    {"positions": ["6,14", "6,13", "6,12", "7,14", "7,13", "7,12"], "roomName": "room_1"},
    {"positions": ["1,13"], "roomName": "room_2"},
    {"positions": ["5,10", "6,10", "7,10"], "roomName": "room_3"},
    {"positions": ["1,8", "1,7", "1,6", "2,8", "2,7", "2,6", "3,8", "3,7", "3,6"], "roomName": "room_4"},
    {"positions": ["1,4"], "roomName": "room_5"},
    {"positions": ["3,4", "3,3", "4,4", "4,3"], "roomName": "room_6"},
    {"positions": ["1,2"], "roomName": "room_7"},
    {"positions": ["7,0","7,1"], "roomName": "room_8"},
    {"positions": ["9,14", "9,13", "9,12", "10,14", "10,13", "10,12", "11,14", "11,13", "11,12"], "roomName": "room_9"},
    {"positions": ["13,11", "13,10", "14,11", "14,10"], "roomName": "room_10"},
    {"positions": ["5,8", "5,7", "5,6", "6,8", "6,7", "6,6", "7,8", "7,7", "7,6"], "roomName": "room_11"},
    {"positions": ["12,7", "12,6", "13,7", "13,6"], "roomName": "room_12"},
    {"positions": ["12,4", "12,3", "12,2", "13,4", "13,3", "13,2", "14,4", "14,3", "14,2"], "roomName": "room_13"},
    {"positions": ["12,0", "13,0", "14,0"], "roomName": "room_14"},
    {"positions": ["6,3","6,4","7,3","8,3","8,4"], "roomName": "room_15"},
]

#creates a list of dictionaries for each of the gate points,
#which are grid locations where the current the player will answer
#a riddle, or a key check will occur.
#each dictionary contains the grid coordinates, the name of the gate/correspodning key name,
#and what the gate is unlocked by
gateRooms = [
        {"positions": ["0,3"], "gateName": "gate_5", "unlocked_by": "riddle", "unlocked": False},
        {"positions": ["4,2"], "gateName": "silver key", "unlocked_by": "key", "unlocked": False},
        {"positions": ["4,10"], "gateName": "gate_11", "unlocked_by": "riddle", "unlocked": False},
        {"positions": ["8,7", "4,7", "6,9"], "gateName": "gold key", "unlocked_by": "key", "unlocked": False},
        {"positions": ["13,1"], "gateName": "gate_14", "unlocked_by": "riddle", "unlocked": False},
        {"positions": ["13,5"], "gateName": "bronze key", "unlocked_by": "key", "unlocked": False}
        ]


#creates a function which checks whether the player is located at a trigger point
def checkForTriggerRoom(player_position):
        
        #sets the variable current_room to global, so it can be updated without being passed/returned
        global current_room

        #Create a new list of matching rooms, where the position is in the positions key in the triggerRooms list
        roomNames = [row for row in triggerRooms if convertToKey(player_position) in row['positions']]

        #checks to see whether the roomNames list is empty, and if not:
        if len(roomNames) > 0:
                
                #the current room gets updates to the name of the room located at the first position in the dictionary
                current_room = roomNames[0]['roomName']

                #displays the current room to the user
                print("You are in" + " " + rooms[current_room]["name"] + "\n")

                #displays the current rooms description to the player
                print(rooms[current_room]["description"] + "\n")

                #checks to see whether there are any items in the current room
                if len(rooms[current_room]["items"]) > 0:

                        #if there are, a loop will iterate through each item and print it's name
                        print("In this room, there is: ", end = "" + "\n")
                        for item in rooms[current_room]["items"]:
                                print(item["name"])
                                
                #otherwise, the message below will print               
                else:
                        print("There are no items here.")
                return current_room
        return None

#creates a function which checks whether the player is located at a gate trigger point
def checkForTriggerGate(player_position, inventory):

        #Create a new list of matching rooms, where the position is in the positions key in the gateRooms list
        gateNames = [row for row in gateRooms if convertToKey(player_position) in row['positions']]

        #checks to see whether the gateNames list is empty, and if not: 
        if len(gateNames) > 0:

                #checks to see whether the gate is already unlocked and if so, the fuction returns True
                if gateNames[0]["unlocked"] == True:
                        return(True)

                #othersise:
                else:
                        #the function checks to see whether the gate is unlocked by a key or a riddle
                        #if the gate is unlocked by a riddle, the function will:
                        print("This gate is opened by a " + gateNames[0]["unlocked_by"])
                        if gateNames[0]["unlocked_by"] == "riddle":

                                #check to see which gate is being triggered
                                if gateNames[0]["gateName"]== "gate_5":
                                        #gets the True or False value depending on the player's answer
                                        result = (riddle(riddle_water))
                                elif gateNames[0]["gateName"] == "gate_11":
                                        result = (riddle(riddle_steps))
                                elif gateNames[0]["gateName"] == "gate_14":
                                       result = (riddle(riddle_clouds))

                                #if the answer is correct, the gate will unlock
                                if result == True:
                                        gateNames[0]["unlocked"] = True
                                        return(result)
                                else:
                                        #otherwise, the gate will remain locked
                                        return(False)

                        #otherwise, if the gate is unlocked via a key:        
                        else:
                                #each item in the inventory is iterated through, and the id is compared with the required key
                                for item in inventory:
                                        if item["id"] == gateNames[0]["gateName"]:
                                                #if a match is found, the gate will unlock, and the player will be notified
                                                print("Gate unlocked by " + gateNames[0]["unlocked_by"])
                                                gateNames[0]["unlocked"] = True
                                                return True

                                #otherwise, the player will be told they need to find the key
                                print("You need to find the key for this room")
                                return False
        return True


#creates a function which retrieves a list of all exits accessible to the player
def getAvailableExits(player_position):
    exits = {}

    #the x and y grid coordinates for the player are assigned to the respective variables
    x = player_position[0]
    y = player_position[1]

    #as 14 is the upper boudary for the grid, the fucntion checks that the move will not move the player outside the boundary
    if x < 14:
        exits["east"] = [x + 1, y]
    if y < 14:
        exits["north"] = [x, y + 1]

    #as 0 is the lower boudary for the grid, the fucntion checks that the move will not move the player outside the boundary
    if x > 0:
        exits["west"] = [x - 1, y]
    if y > 0:
        exits["south"] = [x, y - 1]

    #retruns a dictionary of all the available exits which are not listed in the blocked_exits list
    return {key: value for key, value in exits.items() if convertToKey(value) not in blockedExits}



def convertToKey(player_positionition):
    return ",".join(map(str, player_positionition))

