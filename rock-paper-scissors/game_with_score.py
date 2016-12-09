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
    user_score, computer_score = 0,0

    while user_score < 5 and computer_score < 5:
        computer_choice = random.choice(["rock", "paper", "scissors"])
        user_choice = raw_input("\nChoose rock (r), paper (p), or scissors (s): ").lower()

        if user_choice in options.keys():
            print "\nPlayer chose " + str(options[user_choice]()) + "."
            print "Computer chose " + computer_choice + "."

            if (user_choice == "r" and computer_choice == "rock")\
            or (user_choice == "p" and computer_choice == "paper")\
            or (user_choice == "s" and computer_choice == "scissors"):
                print "\nTie!"
                print "Player Score: {}, Computer Score: {}".format(user_score, computer_score)

            elif user_choice == "r":
                if computer_choice == "paper":
                    computer_score += 1
                    print "\nPaper beats rock, Computer wins!"
                    print "Player Score: {}, Computer Score: {}".format(user_score, computer_score)
                else:
                    user_score += 1
                    print "\nRock beats scissors, Player wins!"
                    print "Player Score: {}, Computer Score: {}".format(user_score, computer_score)

            elif user_choice == "p":
                if computer_choice == "rock":
                    user_score += 1
                    print "\nPaper beats rock, Player wins!"
                    print "Player Score: {}, Computer Score: {}".format(user_score, computer_score)
                else:
                    computer_score += 1
                    print "\nScissors beat paper, Computer wins!"
                    print "Player Score: {}, Computer Score: {}".format(user_score, computer_score)

            else:
                if computer_choice == "rock":
                    computer_score += 1
                    print "\nRock beats scissors, Computer wins!"
                    print "Player Score: {}, Computer Score: {}".format(user_score, computer_score)
                else:
                    user_score += 1
                    print "\nScissors beat paper, Player wins!"
                    print "Player Score: {}, Computer Score: {}".format(user_score, computer_score)

        else:
            print "Invalid entry, try again!"

Game()
