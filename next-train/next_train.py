def Nexttrain():
    trains = [2,5,7.5,8.5,9,10,11.5,13.5,14.5,17,18,19,24]
    user_train = []

    while True:
        try:
            user_time = float(raw_input("What time are you leaving? "))
            break
        except ValueError:
            print "Sorry, I don't understand that time.\n"

    for index, train in enumerate(trains):
        if train > user_time:
            user_train.append([index+1,train])

    print "You should catch Train {} leaving at {}".format(user_train[0][0],user_train[0][1])

    if user_train[0][0] == 13:
        print "\n\
***DON'T STOP...BELIEVIN'!***\n\n\
Just a small town girl\n\
Living in a lonely world\n\
She took the midnight train going anywhere\n\
Just a city boy\n\
Born and raised in South Detroit\n\
He took the midnight train going anywhere\n\n\
A singer in a smoky room\n\
A smell of wine and cheap perfume\n\
For a smile they can share the night\n\
It goes on and on and on and on\n\n\
Strangers waiting, up and down the boulevard\n\
Their shadows searching in the night\n\
Streetlights people, living just to find emotion\n\
Hiding, somewhere in the night."

Nexttrain()
