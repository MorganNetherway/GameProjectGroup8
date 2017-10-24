import string
#README
#This file takes on the functionality of GAMEPARSER.py but with some added functionality.
#As well as removing whitespace, punctuation and useless words, it also translates useful
#words into command words to be used later.
#feel free to update this list as you see fit
#
#
#To call this file, just call normalise_input() as usual.




#list of important words - see below for their translations


attack_words = ["attack", "stab", "wound", "injure", "stab", "shiv", "punch",
               "slice", "cut", "battle", "engage", "combat", "batter", "beat",
               "pummel", "beat up", "strike", "pound", "thrash", "inflict",
               "tackle", "kill"]

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

take_words = ["take", "equip", "claim"]

drop_words = ["drop", "abandon", "leave"]

sword_words = ["sword"]



#translations of important words into functional command words

word_translations = {
    "attack": attack_words,
    "block": block_words,
    "flee": flee_words,
    "use": use_words,
    "go": movement_words,
    "north": north_words,
    "south": south_words,
    "east": east_words, 
    "west": west_words,
    "take": take_words,
    "drop": drop_words,
    "sword": sword_words
    }

#function which translates important words into useful command words AFTER
#unimportant words have been removed

def translate_words(user_input):
    output = []
    for input_item in user_input:
        for word_group in word_translations:
            for word in word_translations[word_group]:
                if word == input_item:
                    output.append(word_group)

    return output


# List of "unimportant" words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']


def filter_words(words, skip_words):
    """This function takes a list of words and returns a copy of the list from
    which all words provided in the list skip_words have been removed.
    For example:

    >>> filter_words(["help", "me", "please"], ["me", "please"])
    ['help']

    >>> filter_words(["go", "south"], skip_words)
    ['go', 'south']

    >>> filter_words(['how', 'about', 'i', 'go', 'through', 'that', 'little', 'passage', 'to', 'the', 'south'], skip_words)
    ['go', 'passage', 'south']

    """
    checked_words = []
    for i in range(0, len(words)):
        for j in range(0, len(skip_words)):
            if words[i] == skip_words[j]:
                break
            elif words[i] != skip_words[j] and j == len(skip_words)-1:
                checked_words.append(words[i])
                
    return checked_words
 
        

    
def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation. For example:

    >>> remove_punct("Hello, World!")
    'Hello World'
    >>> remove_punct("-- ...Hey! -- Yes?!...")
    ' Hey  Yes'
    >>> remove_punct(",go!So.?uTh")
    'goSouTh'
    """
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct


def normalise_input(user_input):
    """This function removes all punctuation from the string and converts it to
    lower case. It then splits the string into a list of words (also removing
    any extra spaces between words) and further removes all "unimportant"
    words from the list of words using the filter_words() function. The
    resulting list of "important" words is returned. For example:

    >>> normalise_input("  Go   south! ")
    ['go', 'south']
    >>> normalise_input("!!!  tAkE,.    LAmp!?! ")
    ['take', 'lamp']
    >>> normalise_input("HELP!!!!!!!")
    ['help']
    >>> normalise_input("Now, drop the sword please.")
    ['drop', 'sword']
    >>> normalise_input("Kill ~ tHe :-  gObLiN,. wiTH my SWORD!!!")
    ['kill', 'goblin', 'sword']
    >>> normalise_input("I would like to drop my laptop here.")
    ['drop', 'laptop']
    >>> normalise_input("I wish to take this large gem now!")
    ['take', 'gem']
    >>> normalise_input("How about I go through that little passage to the south...")
    ['go', 'passage', 'south']

    """
    # Remove punctuation and convert to lower case
    no_punct = remove_punct(user_input).lower()
    no_punct_list = []
    i = 0

    no_punct.strip()

    no_punct = no_punct.split()

    filtered = filter_words(no_punct, skip_words)

    command_words = translate_words(filtered)

    return command_words



    

                
