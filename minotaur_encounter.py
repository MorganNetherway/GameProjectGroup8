import random
from player import * #file containing variables for the players health, attack and defence after modification from items
from minotaur import * #file containing the health and atatck for the minotaur
from word_translation import * #normalising the player's input
from ascii_art import *


def encounter_push():
    #picks randomly between 0 and 1

    global minotaur_health
    global player_stats
    
    pushvar = random.randint(0, 1)
    if pushvar == 1:
        print('''You charge headfirst at the minotaur, shoving him into the well.
        After a few seconds you hear a thud. Your foe lies dead at the bottom of
        the deep cavern below. You have won!''')
        minotaur_stats["health"] = 0
    else:
        damage_dealt = minotaur_stats["attack"] - player_stats["defense"]
        print("You charge at the minotaur and miss! The minotaur strikes you for" + str(damage_dealt) + "damage!")
        player_stats["health"] -= damage_dealt
     
    return

def encounter_run():
    #picks randomly between 0 and 1
    escape = random.randint(0, 1)
    
    #if escape is equal to 1, the player will escape
    if escape == 1:
        player_input = input("You see your chance to escape and take it\n Which direction do you take?:\n")
        return player_input
        
    #otherwise, the player will have to attack the minotaur, and the encounter_attack function will run
    else:
        print("The minotaur sees you move and blocks your escape! You have no choice but to fight!")
        encounter_attack()

def encounter_attack():
    #access and save the health amount of the player and minotaur
    global minotaur_stats
    global player_stats
        
    #calculates the damage the player takes, based upon the minotaur's attack minus the defence value of the player (with items)
    damage_dealt = minotaur_stats["attack"] - player_stats["defense"]
    
    #updates the player's health
    player_stats["health"] -= damage_dealt
    print("You have been struck by the minotaur for " + str(damage_dealt) + " damage.")
    print("Your health is now " + str(player_stats["health"]) + ".")
    
    #reduces the minotaur's health by the player's attack
    minotaur_stats["health"] -= player_stats["attack"]
    print("You have struck the minotaur for " + str(player_stats["attack"]) + " damage.")
    print("The minotaur's health is now " + str(minotaur_stats["health"]) + ".")
    return

def encounter(player_position):
    print(art_minotaur)
    print("Minotaur encountered!\n")
    print('''You can:
    ATTACK the minotaur
    RUN from the minotaur''')

    #checks if push command is available
    if player_position[0] == 1 or player_position[0] == 2 or player_position[0] == 3:
        if player_position[1] == 6 or player_position[1] == 7 or player_position[1] == 8:
            print('PUSH the minotaur')

    #takes the players chosen command
    player_input = input("What would you like to do?!?:\n")

    #normalises the player's input and runs the corresponding function
    while True:
        if "push" in normalise_input(player_input):
            encounter_push()
            return
            
        elif "attack" in normalise_input(player_input):
            encounter_attack()
            return
            
        elif "flee" in normalise_input(player_input):
            encounter_run()
            return

        else:
            print('''You can:
        ATTACK the minotaur
        RUN from the minotaur
    What would you like to do?!?:''')

        player_input = input("What would you like to do?!?:\n")
    

