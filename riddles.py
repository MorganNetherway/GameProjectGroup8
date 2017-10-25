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


def riddle(riddle_id):
    print(riddle_id["text"])
    user_input = input("> ")
    #make sure to normalize the user input
    if user_input == riddle_id["answer"]:
        print("You are correct!")
        return(True)
    else:
        print("You have answered incorrectly!")
        return(False)
