


attack_words = ["attack", "stab", "wound", "injure", "stab", "shiv", "punch",
               "slice", "cut", "battle", "engage", "combat", "batter", "beat",
               "pummel", "beat up", "strike", "pound", "thrash", "inflict",
               "tackle"]

block_words = ["block", "deflect", "shield", "repel", "parry", "counter"]

flee_words = ["run", "sprint", "escape", "flee", "retreat", "bolt", "abscond"]

use_words = ["use", "utilise", "operate", "apply", "cast", "drink"]

movement_words = ["go", "travel", "move", "walk", "amble", "wander", "sneak",
                 "advance", "progress", "locomote", "proceed"]

north_words = ["north", "forwards", "up", "straight", "northwardly", "northwards",
              "northernly", "upwards"]

south_words = ["south", "back", "backwards", "down", "downwards", "southwards",
             "southwardly", "backwards"]

east_words = ["east", "eastwardly", "eastwards", "right"]

west_words = ["west", "westwardly", "westwards", "left"]


word_translations = {
    "attack": attack_words,
    "block": block_words,
    "flee": flee_words,
    "use": use_words,
    "go": movement_words,
    "north": north_words,
    "south": south_words,
    "east": east_words, 
    "west": west_words
    }


def translate_words(user_input):
    output = "that doesn't make any sense"
    for word_group in word_translations:
        for word in word_translations[word_group]:
            if word == user_input:
                output = word_group

    return output
        




print(translate_words("run"))















    

                
