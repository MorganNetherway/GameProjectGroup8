from player import * #file containing variables for the players health, attack and defence after modification from items
from minotaur import * #file containing the health and atatck for the minotaur

def encounter():
    global player_health
    global minotaur_health
    
    #checks to see whether the player and minotaur are in the same loction
    if minotaur_current_location == player_current_location:
        
        #calculates the damage the player takes, based upon the minotaur's attack minus the defence value of the player (with items)
        damage_dealt = minotaur_attack - player_defense
        
        #updates the player's health
        player_health -= damage_dealt
        
        #reduces the minotaur's health by the player's attack
        minotaur_health -= player_attack
        return

    return
