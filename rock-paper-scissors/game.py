import random

def Rock():
    return "rock"

def Paper():
    return "paper"

def Scissors():
    return "scissors"

options = {"r": Rock,
            "p": Paper,
            "s": Scissors}

def Game():
    computer_score, user_score = 0,0
    computer_choice = random.choice(["rock", "paper", "scissors"])
    user_choice = raw_input("Choose rock (r), paper (p), or scissors (s): ").lower()

    if user_choice in options.keys():
        print "Player chose " + str(options[user_choice]()) + "."
        print "Computer chose " + computer_choice + "."

        if (user_choice == "r" and computer_choice == "rock")\
        or (user_choice == "p" and computer_choice == "paper")\
        or (user_choice == "s" and computer_choice == "scissors"):
            print "Tie!"
        elif user_choice == "r" and computer_choice == "paper":
            print "Paper beats rock, Computer wins!"
        elif user_choice == "r" and computer_choice == "scissors":
            print "Rock beats scissors, Player wins!"
        elif user_choice == "p" and computer_choice == "rock":
            print "Paper beats rock, Player wins!"
        elif user_choice == "p" and computer_choice == "scissors":
            print "Scissors beat paper, Computer wins!"
        elif user_choice == "s" and computer_choice == "rock":
            print "Rock beats scissors, Computer wins!"
        elif user_choice == "s" and computer_choice == "paper":
            print "Scissors beat paper, Player wins!"
    else:
        print "Invalid entry, try again!"

Game()
