import random
from player import *
from rooms import *
from riddles import *

current_room = None

blockedExits = [
    "0,14", "0,13", "0,12", "0,11",
    "1,14", "1,12", "1,11", "1,9", "1,5", "1,3", "1,1",
    "2,14", "2,9", "2,7", "2,5", "2,4", "2,3", "2,2", "2,1",
    "3,14", "3,12", "3,11", "3,9", "3,5", "3,2", "3,1",
    "4,14", "4,12", "4,11", "4,9", "4,8", "4,6", "4,5",
    "5,14", "5,12", "5,11", "5,9", "5,5", "5,4", "5,3", "5,2", "5,0",
    "6,6", "6,5", "6,2", "6,0",
    "7,11","7,9", "7,5", "7,4", "7,2",
    "8,14", "8,12", "8,11", "8,10", "8,9", "8,8", "8,6", "8,5", "8,2", "8,0",
    "9,11", "9,6", "9,5", "9,4", "9,0",
    "10,13", "10,11", "10,9", "10,8", "10,7", "10,6", "10,5", "10,4", "10,2", "10,1", "10,0",
    "11,11", "11,9", "11,8", "11,7", "11,6", "11,5", "11,4", "11,2", "11,1", "11,0",
    "12,13", "12,12", "12,11", "12,5", "12,1",
    "13,13", "13,12", "13,9", "13,8",
    "14,9", "14,8", "14,7", "14,6", "14,5", "14,1"
]



triggerRooms = [
    {"positions": ["2,7"], "roomName": "special_well"},
    {"positions": ["6,14", "6,13", "6,12", "7,14", "7,13", "7,12"], "roomName": "room_1"},
    {"positions": ["1,13"], "roomName": "room_2"},
    {"positions": ["5,10", "6,10", "7,10"], "roomName": "room_3"},
    {"positions": ["1,8", "1,7", "1,6", "2,8", "2,7", "2,6", "3,8", "3,7", "3,6"], "roomName": "room_4"},
    {"positions": ["1,4"], "roomName": "room_5"},
    {"positions": ["3,4", "3,3", "4,4", "4,3"], "roomName": "room_6"},
    {"positions": ["1,3"], "roomName": "room_7"},
    {"positions": ["8,0"], "roomName": "room_8"},
    {"positions": ["9,14", "9,13", "9,12", "10,14", "10,13", "10,12", "11,14", "11,13", "11,12"], "roomName": "room_9"},
    {"positions": ["13,11", "13,10", "14,11", "14,10"], "roomName": "room_10"},
    {"positions": ["5,8", "5,7", "5,6", "6,8", "6,7", "6,6", "7,8", "7,7", "7,6"], "roomName": "room_11"},
    {"positions": ["12,7", "12,6", "13,7", "13,6"], "roomName": "room_12"},
    {"positions": ["12,4", "12,3", "12,2", "13,4", "13,3", "13,2", "14,4", "14,3", "14,2"], "roomName": "room_13"},
    {"positions": ["12,0", "13,0", "14,0"], "roomName": "room_14"},
    #{"positions": ["4,10"], "roomName": "gate_1"},
    #{"positions": ["6,9"], "roomName": "gate_2"},
    #{"positions": ["4,7"], "roomName": "gate_3"},
    #{"positions": ["8,7"], "roomName": "gate_4"},
    #{"positions": ["4,2"], "roomName": "gate_5"}
]

gateRooms = [
        {"positions": ["0,3"], "gateName": "gate_5", "unlocked_by": "riddle", "unlocked": False},
        {"positions": ["4,2"], "gateName": "gate_6", "unlocked_by": "key", "unlocked": False},
        {"positions": ["4,10"], "gateName": "gate_3", "unlocked_by": "riddle", "unlocked": False},
        {"positions": ["8,7", "4,7", "6,9"], "gateName": "gate_11", "unlocked_by": "key", "unlocked": False},
        {"positions": ["13,1"], "gateName": "gate_14", "unlocked_by": "riddle", "unlocked": False},
        {"positions": ["13,5"], "gateName": "gate_12", "unlocked_by": "key", "unlocked": False}
        ]


def checkForTriggerRoom(player_position):
        global current_room
        roomNames = [row for row in triggerRooms if convertToKey(player_position) in row['positions']] #Create a new list of matching rooms, where the position is in the po
        if len(roomNames) > 0:
                current_room = roomNames[0]['roomName']
                print("You are in" + " " + rooms[current_room]["name"] + "\n")
                print(rooms[current_room]["description"] + "\n")
                print("In this room, there is: ", end = "")
                for item in rooms[current_room]["items"]:
                        print(item["name"])
                return current_room
        return None

def checkForTriggerGate(player_position, inventory):
        gateNames = [row for row in gateRooms if convertToKey(player_position) in row['positions']]
        if len(gateNames) > 0:
                if gateNames[0]["unlocked"] == True:
                        return(True)
                else:
                        print("This gate is opened by a " + gateNames[0]["unlocked_by"])
                        if gateNames[0]["unlocked_by"] == "riddle":
                                if gateNames[0]["gateName"]== "gate_5":
                                        result = (riddle(riddle_water))
                                elif gateNames[0]["gateName"] == "gate_3":
                                        result = (riddle(riddle_steps))
                                else:
                                       result = (riddle(riddle_clouds)) 
                                if result == True:
                                        gateNames[0]["unlocked"] = True
                                        return(result)
                                else:
                                        return(False)
                        else:
                                for item in inventory:
                                        print(item["name"])
                                        print(gateNames[0]["gateName"] + " unlocked by " + gateNames[0]["unlocked_by"])
                                        if item["id"] == gateNames[0]["gateName"]:
                                                return True
                                print("You need to find the key for this room")
                                return False
        return True



def getAvailableExits(player_position):
    exits = {}
    x = player_position[0]
    y = player_position[1]
    if x < 14:
        exits["east"] = [x + 1, y]
    if y < 14:
        exits["north"] = [x, y + 1]
    if x > 0:
        exits["west"] = [x - 1, y]
    if y > 0:
        exits["south"] = [x, y - 1]
    return {key: value for key, value in exits.items() if convertToKey(value) not in blockedExits}

def convertToKey(player_positionition):
    return ",".join(map(str, player_positionition))





def testFunc():
    print (getAvailableExits([14,11])) #{'north': [14, 12], 'west': [13, 11], 'south': [14, 10]}
    print (getAvailableExits([7,0])) #{'east': [7, 1]}
    print (getAvailableExits([0,0])) #{'east': [1, 0], 'north': [0, 1]}
    print (minAvailableExits[random.choice(list(getAvailableExits(minPos).keys()))])
