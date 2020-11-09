from random import randint

def suckies(password):
    if password==69420:
        whoSucks= []
        for i in range(5):
            j = randint(0,2)
            if j==0:
                whoSucks.append("gaiusSucks")
            if j==1:
                whoSucks.append("zekeSucks")
        zekeSucks = 0
        gaiusSucks = 0
        for i in whoSucks:
            if i == "gaiusSucks":
                gaiusSucks += 1
            if i == "zekeSucks":
                zekeSucks += 1
        if zekeSucks >= 3:
            print("zeke sucks more")
        elif gaiusSucks >= 3:
            print("gaius sucks more")
        else:
            print ("neither")

suckies(69420)
