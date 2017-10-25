#import the rooms file
from rooms import *
from movement import *
import random
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


#the current health for the minotaur
minotaur_health = 100

#the base damage the player will take
minotaur_attack = 25

#minotaur starts at ..........
minotaur_position = [6,7]

#minotaur's movement speed 0.5: every two turns, 0.25: every four turns etc.
minotaur_movement_speed = 1
def minotaurMove(minotaur_position, minAvailableExits):
    return minAvailableExits[random.choice(list(getAvailableExits(minotaur_position).keys()))]
