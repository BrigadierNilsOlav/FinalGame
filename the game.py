def delay_print_stage(s):
    for char in s:
        print(char, end='')
        time.sleep(0.2)
def delay_print_text(s):
    for char in s:
        print(char, end='')
        time.sleep(0.05)

import time
from time import sleep
from threading import Timer
timeout = 3
timeout1 = 3

print("""
*************************************
*************************************
**    .                     .      **
** .      DUNGEON OF TERROR        **
**             .               .   **
**    .               .            **
**         .                 .     **                                    
**  .             .                **
*************************************
*************************************
""")
#SETUP
print("SETUP")
print("Type your name below ...")
setupname = input()
print("Reading your name...")
sleep(1)
print("Remembering your name...")
sleep(1)
print("Okay, {}.".format(setupname))

delay_print_stage("...STAGE 1...")
delay_print_text("""
-DUNGEON ENTRANCE
""")
print("""
##################
#    CONTROLS    #
#                #
#  W - Forward   #
#  A - Left      #
#  S - Back      #
#  D - Right     #
#                #
##################

TYPE START
""")
starting = input()
if starting in "start START":
    directionother = "back"
    while directionother == "back":
        directionother2 = "n"
        while directionother2 == "n":
        
            print("Which way would you like to go? W/A/S/D")
            direction1 = input()

            if direction1 == "w":
                print("You walk forward further into the dungeon.")

            if direction1 == "s":
                print("leaving so soon? y/n")
                directionother2 = input()
                if directionother2 == "y":
                    exit()

            if direction1 == "a":
                print("you walked into a wall. you realized that the passageway youre in is extremely tight. (hint)")
                print("type back to go back")
                directionother = input()

            if direction1 == "d":
                print("you walked into a wall. you realized that the passageway youre in is extremely tight. (hint)")
                print("type back to go back")
                directionother = input()
