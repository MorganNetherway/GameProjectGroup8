import random
from rooms import *
blockedExits = [
    "0,14", "0,13", "0,12", "0,11",
    "1,14", "1,12", "1,11", "1,9", "1,5", "1,3", "1,1",
    "2,14", "2,9", "2,7", "2,5", "2,4", "2,3", "2,2", "2,1",
    "3,14", "3,12", "3,11", "3,9", "3,5", "3,2", "3,1",
    "4,14", "4,12", "4,11", "4,9", "4,8", "4,6", "4,5",
    "5,14", "5,12", "5,11", "5,9", "5,5", "5,4", "5,3", "5,2", "5,0",
    "6,5", "6,2", "6,0",
    "7,11", "7,9", "7,5", "7,4", "7,2",
    "8,14", "8,12", "8,11", "8,9", "8,8", "8,6", "8,5", "8,2", "8,0",
    "9,11", "9,6", "9,5", "9,4", "9,0",
    "10,13", "10,11", "10,9", "10,8", "10,7", "10,6", "10,5", "10,4", "10,2", "10,1", "10,0",
    "11,11", "11,9", "11,8", "11,7", "11,6", "11,5", "11,4", "11,2", "11,1", "11,0",
    "12,13", "12,12", "12,11", "12,5", "12,1",
    "13,13", "13,12", "13,9", "13,8",
    "14,9", "14,8", "14,7", "14,6", "14,5", "14,1"
]



triggerRooms = [
    {"positions": ["2,7"], "action": special_well},
    {"positions": ["6,14", "6,13", "6,12", "7,14", "7,13", "7,12"], "action": room_1},
    {"positions": ["1,13"], "action": room_2},
    {"positions": ["5,10", "6,10", "7,10"], "action": room_3},
    {"positions": ["1,8", "1,7", "1,6", "2,8", "2,7", "2,6", "3,8", "3,7", "3,6"], "action": room_4},
    {"positions": ["1,4"], "action": room_5},
    {"positions": ["3,4", "3,3", "4,4", "4,3"], "action": room_6},
    {"positions": ["1,3"], "action": room_7},
    {"positions": ["8,0"], "action": room_8},
    {"positions": ["9,14", "9,13", "9,12", "10,14", "10,13", "10,12", "11,14", "11,13", "11,12"], "action": room_9},
    {"positions": ["13,11", "13,10", "14,11", "14,10"], "action": room_10},
    {"positions": ["5,8", "5,7", "5,6", "6,8", "6,7", "6,6", "7,8", "7,7", "7,6"], "action": room_11},
    {"positions": ["12,7", "12,6", "13,7", "13,6"], "action": room_12},
    {"positions": ["12,4", "12,3", "12,2", "13,4", "13,3", "13,2", "14,4", "14,3", "14,2"], "action": room_13},
    {"positions": ["12,0", "13,0", "14,0"], "action": room_14},
    {"positions": ["4,10"], "action": gate_1},
    {"positions": ["6,9"], "action": gate_2},
    {"positions": ["4,7"], "action": gate_3},
    {"positions": ["8,7"], "action": gate_4},
    {"positions": ["4,2"], "action": gate_5}
]


def checkForTriggerRoom(player_position):
        relevantTriggers = [row for row in triggerRooms if convertToKey(player_position) in row['positions']]
        for trigger in relevantTriggers:
            trigger['action']()

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
