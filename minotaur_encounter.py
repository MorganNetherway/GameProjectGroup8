import random
from player import * #file containing variables for the players health, attack and defence after modification from items
from minotaur import * #file containing the health and atatck for the minotaur
from gameparser import * #normalising the player's input

def encounter_push():
    pass

def encounter_run():
    #picks randomly between 0 and 1
    escape = random.randint(0, 1)
    
    #if escape is equal to 1, the player will escape
    if escape == 1:
        print("You escaped")
        
    #otherwise, the player will have to attack the minotaur, and the encounter_attack function will run
    else:
        print("Escape failed. You will have to attack the minotaur.")
        encounter_attack()

def encounter_attack():
    #access and save the health amount of the player and minotaur
    global player_health
    global minotaur_health
        
    #calculates the damage the player takes, based upon the minotaur's attack minus the defence value of the player (with items)
    damage_dealt = minotaur_attack - player_defense
    
    #updates the player's health
    player_health -= damage_dealt
    print("You have been struck by the minotaur for " + str(damage_dealt) + " damage.")
    print("Your health is now " + str(player_health) + ".")
    
    #reduces the minotaur's health by the player's attack
    minotaur_health -= player_attack
    print("You have struck the minotaur for " + str(player_attack) + " damage.")
    print("The minotaur's health is now " + str(minotaur_health) + ".")
    return

def encounter():
    print("Minotaur encountered!\n")
    print('''You can:
    ATTACK the minotaur
    RUN from the minotaur
    PUSH the minotaur''')

    #takes the players chosen command
    player_input = input("What do you want to do:\n")

    #normalises the player's input and runs the corresponding function
    if normalise_input(player_input) == ["push"]:
        encounter_push()
        
    elif normalise_input(player_input) == ["attack"]:
        encounter_attack()
        
    elif normalise_input(player_input) == ["run"]:
        encounter_run()

