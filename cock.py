from random import randint

def suckies(password):
    if password==69420:
        gaiusSucks = 0
        zekeSucks = 0
        for i in range(5):
            random = randint (0, 10)
            gaiusSucks += random
            random = randint (0, 10)
            zekeSucks += random
        if gaiusSucks > zekeSucks:
            print ("Gaius sucks more")
        elif zekeSucks > gaiusSucks:
            print ("Zeke sucks more")
        else:
            print ("Both suck eachother")


suckies(69420)
        
