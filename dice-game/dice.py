def DiceGame():
    import random

    play = True
    while play:
        number1 = random.randrange(1,7)
        number2 = random.randrange(1,7)
        print "You rolled a {} and a {}".format(number1,number2)
        print "Total: {}".format(number1+number2)
        cont_game = raw_input("Press 'Enter' to roll again, 'S' to stop ")
        print ""
        if cont_game == "S":
            play = False

DiceGame()
