def DiceGame():
    import random

    user_input1 = int(raw_input("How many sides does your dice have? "))
    user_input2 = int(raw_input("How many times would you like to roll your pair of dice? "))
    print ""

    while True:
        total = 0
        while total < user_input2:
            num1 = random.randrange(1,user_input1+1)
            num2 = random.randrange(1,user_input1+1)

            print "You rolled a {} and a {}. Total: {}".format(num1,num2,num1+num2)
            total += 1

        cont_game = raw_input("\nRoll Again? (Y/N)> ")
        print ""

        if cont_game == "N":
            break

DiceGame()
