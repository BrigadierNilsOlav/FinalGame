def backpack():
    print("")
    print("{}, {}, and {}.".format(backpacka1, backpacka2, backpacka3))
    print("what item do you want to use against the enemy?")

def backpack1():
    print("")
    print("{}, {}, and {}.".format(backpackb1, backpackb2, backpackb3))
    print("what item do you want to use against the enemy?")


import random
backpacklista1 = "a toothbrush", "a butchers knife", "a baseball bat", "a crowbar", "a cricket bat", "a lead pipe", "a sword", "a mace", "a sharpened straw", "a spoon"
backpacklista2 = "a piece of bread", "a cookie", "a tim tam", "a strange liquid", "a fermented potato", "a biscuit", "an entire pig", "a pile of magic beans"
backpacklista3 = "a fireball", "a lightning bolt", "a pepper spray", "a lazer tag gun", "a spitball", "a pile of darts", "a bear summoner"
backpacka1 = random.choice(backpacklista1)
backpacka2 = random.choice(backpacklista2)
backpacka3 = random.choice(backpacklista3)
killmessages = "the enemy succumbed to their injuries and died", "you brutally destroyed the enemies throat with your tool", "you absolutely demolished the enemy and then planted a flag in his chest to assert dominance"
killmessage = random.choice(killmessages)

backpacklistb1 = "a toothbrush", "a butchers knife", "a baseball bat", "a crowbar", "a cricket bat", "a lead pipe", "a sword", "a mace", "a sharpened straw", "a spoon"
backpacklistb2 = "a piece of bread", "a cookie", "a tim tam", "a strange liquid", "a fermented potato", "a biscuit", "an entire pig", "a pile of magic beans"
backpacklistb3 = "a fireball", "a lightning bolt", "a pepper spray", "a lazer tag gun", "a spitball", "a pile of darts", "a bear summoner"
backpackb1 = random.choice(backpacklistb1)
backpackb2 = random.choice(backpacklistb2)
backpackb3 = random.choice(backpacklistb3)
killmessages = "the enemy succumbed to their injuries and died", "you brutally destroyed the enemies throat with your tool", "you absolutely demolished the enemy and then planted a flag in his chest to assert dominance"
killmessage = random.choice(killmessages)



print("STAGE 1")
print("Dungeon Entrance")
print("""
====================================
ENEMY                          ENEMY
================   =================
               |   |
               |   |
               |   |
               |   |
               |   |
               |   |
               |   |
               |   |
               |   |
               |   |
               |you|
""")
print("LEFT/RIGHT")
leftrightinput = input()
if leftrightinput == "left":
    print("You turned left and theres an enemy standing ahead of you. You check your backpack and there are 3 items inside.")
    backpack()
    backpackchoice = input()
    if backpackchoice in backpacklista2:
        print("food is not effective against enemies you imbecile")
    if backpackchoice in backpacklista3:
        print("you used {} against the enemy".format(backpacka3))
        print(killmessage)

        print("RIGHT/BACK")
        rightbackinput = input()

        if rightbackinput == "back":
            print("you turned back and went back to the start of the cave, you're either crying or you just need a break")
            print("you can now eat with the E key")

        elif rightbackinput == "right":
            print("You turn right and walk forwards and theres an enemy standing ahead of you. You check your backpack and you noticed theres new items inside the backpack that weren't there before. 'that's odd', you think.")
            backpack1()
            backpackchoice2 = input()
            if backpackchoice2 in backpacklistb1:
                print("you used {} against the enemy".format(backpackb1))
                print(killmessage)
            if backpackchoice2 in backpacklistb2:
                print("food is not effective against enimes you imbecile")
            if backpackchoice2 in backpacklistb3:
                print("you used {} against the enemy".format(backpackb3))
                print(killmessage)

        if rightbackinput == "back":
            print("you turned back and went back to the start of the cave, you're either crying or you just need a break")
            print("you can now eat with the E key")

        elif rightbackinput == "right":
            print("You turn right and walk forwards and theres an enemy standing ahead of you. You check your backpack and you noticed theres new items inside the backpack that weren't there before. 'that's odd', you think.")
            backpack1()
            backpackchoice2 = input()

    if backpackchoice in backpacklista1:
        print("you used {} against the enemy".format(backpacka1))
        print(killmessage)
        print("RIGHT/BACK")
        rightbackinput = input()

        if rightbackinput == "back":
            print("you turned back and went back to the start of the cave, you're either crying or you just need a break")
            print("you can now eat with the E key")

        elif rightbackinput == "right":
            print("You turn right and walk forwards and theres an enemy standing ahead of you. You check your backpack and you noticed theres new items inside the backpack that weren't there before. 'that's odd', you think.")
            backpack1()
            backpackchoice2 = input()
            if backpackchoice2 in backpacklistb1:
                print("you used {} against the enemy".format(backpackb1))
                print(killmessage)
            if backpackchoice2 in backpacklistb2:
                print("food is not effective against enimes you imbecile")
            if backpackchoice2 in backpacklistb3:
                print("you used {} against the enemy".format(backpackb3))
                print(killmessage)
if leftrightinput == "right":
    print("You turned right and theres an enemy standing ahead of you. You check your backpack and there are 3 items inside.")
    backpack()
    backpackchoice = input()
    if backpackchoice in backpacklista1:
        print("you used {} against the enemy".format(backpacka1))
        print(killmessage)
    if backpackchoice in backpacklista2:
        print("food is not effective against enemies you imbecile")
    if backpackchoice in backpacklista3:
        print("you used {} against the enemy".format(backpacka3))
        print(killmessage)

        print("LEFT/BACK")
        rightbackinput = input()

        if rightbackinput == "back":
            print("you turned back and went back to the start of the cave, you're either crying or you just need a break")
            print("you can now eat with the E key")

        elif rightbackinput == "left":
            print("You turn left and walk forwards and theres an enemy standing ahead of you. You check your backpack and you noticed theres new items inside the backpack that weren't there before. 'that's odd', you think.")
            backpack1()
            backpackchoice2 = input()
