def Fizzbuzz():
    number = list(range(1,101))

    for num in number:
        if num % 3 == 0 and num % 5 == 0:
            print "Fizzbuzz"
        elif num % 3 == 0:
            print "Fizz"
        elif num % 5 == 0:
            print "Buzz"
        else:
            print num

Fizzbuzz()
