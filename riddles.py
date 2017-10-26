from word_translation import *

#creates a dictionary with the riddle question and answer
riddle_water = {
    "text": "You can see me in water, but I never get wet. What am I?",
    "answer": "reflection"
}

riddle_steps = {
    "text": "The more you take, the more you leave behind. What am I?",
    "answer": "footsteps"
}

riddle_clouds = {
    "text": "I fly without wings, I cry without eyes. What am I?",
    "answer": "cloud"
}

#creates a function that takes the riddle dictionary as an input
def riddle(riddle_id):

    #the riddle question is asked
    print(riddle_id["text"])

    #the user input is collected
    user_input = input("> ")
    
    #make sure to normalize the user input
    normalised_input = normalise_input(user_input)

    #checks that the normalised input is the same as the
    #answer located in the dictionary
    if len(normalised_input) == 0:
        normalised_input = "wrong"
    if normalised_input[0] == riddle_id["answer"]:
        print("You are correct!")
        return(True)
    else:
        print("You have answered incorrectly!")
        return(False)
