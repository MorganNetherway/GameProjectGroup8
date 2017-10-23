riddle_water = {
    "text": "You can see me in water, but I never get wet. What am I?",
    "answer": "reflection",
    "switch": False
}

riddle_steps = {
    "text": "The more you take, the more you leave behind. What am I?",
    "answer": "footsteps",
    "switch": False
}

riddle_clouds = {
    "text": "I fly without wings, I cry without eyes. What am I?",
    "answer": "cloud",
    "switch" False
}


def riddle(riddle_id):
    print(riddle_id["text"])
    user_input = input("> ")
    #make sure to normalize the user input
    if user_input == riddle_id["answer"]:
        print("You are correct")
        riddle_id["switch"] = True
        #changes the value "switch" to true, this value can be used to control a door or a chest
        return
    else:
        print("You have answered incorrectly")
        return
