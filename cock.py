from random import randint
gaiusSucks = 0
zekeSucks = 0

def suckies(password):
    if password==69420:
        for i in range(5):
            random = randint (0, 10)
            gaiusSucks += random
            random = randint (0, 10)
            zekeSucks += random
        if gaiusSucks > zekeSucks:
            return "Gaius sucks more"
        elif zekeSucks > gaiusSucks:
            return "Zeke sucks more"
        else:
            return "Both suck eachother"

        
suckies(69420)

        
