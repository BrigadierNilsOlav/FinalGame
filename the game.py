import random
import time
from time import sleep
from threading import Timer

## Random Weapons Selector

weapons = "gun", "knife", "baseball bat", "screwdriver"

weaponchosen = random.choice(weapons)

## Functions, including a delay and loop function

def delay_print_stage(s):
    for char in s:
        print(char, end='')
        time.sleep(0.2)
def delay_print_text(s):
    for char in s:
        print(char, end='')
        time.sleep(0.05)

def wallhit():
    print("you hit a wall as you walk forward.")
    print("YOU HAVE BEEN RESET BACK TO THE START")
    print("type back to go back")
    directionother = input()



1
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

## Setup

print("SETUP")
print("Type your name below ...")
setupname = input()
print("Reading your name...")
sleep(1)
print("Remembering your name...")
sleep(1)
print("Okay, {}.".format(setupname))
print("your randomly selected weapon is.... a {}".format(weaponchosen))

delay_print_stage("...STAGE 1...")
delay_print_text("""
-DUNGEON ENTRANCE
""")

## Game Controls

print("""
##################
#    CONTROLS    #
#                #
#  W - Forward   #
#  A - Left      #      
#  D - Right     #
#                #
##################

TYPE START
""")
starting = input()

## A little introduction to the game

if starting in "start START":
    print("the game is basically simple except your character is blind, therefore if you hit a wall you will be brought back to the start. you also cant turn backwards.")
    print("the game is about trial and error")
    directionother = "back"
    while directionother == "back":
            ## Directional input where you choose which way to go        
            print("Which way would you like to go? W/A/D")
            direction1 = input()

            if direction1 == "w":
                print("You walk forward further into the dungeon.")
                print("Which way would you like to go? W/A/D")
                direction1b = input()
                if direction1b == "w":
                    print("You walk forward further into the dungeon.")
                    print("Which way would you like to go? W/A/D")
                    direction1c = input()
                    if direction1c == "w":
                        print("You walk forward further into the dungeon.")
                        print("Which way would you like to go? W/A/D")
                        direction1d = input()
                        ## Walking into a wall reset loop
                        if direction1d == "w":
                                print("you walked into a wall.")
                                print("YOU HAVE BEEN RESET BACK TO THE START")
                                print("type back to go back")
                                directionother = input()
                        if direction1d == "a":
                                print("you walked left")
                        if direction1d == "d":
                                print("you walked right")
                        

                                
            if direction1 == "a":
                print("you hit a wall as you walked left.")
                print("YOU HAVE BEEN RESET BACK TO THE START")
                print("type back to go back")
                directionother = input()
                if directionother == "51XL1T3RGTR":
                    cheatengine()
            if direction1 == "d":
                print("you hit a wall as you walked right.")
                print("YOU HAVE BEEN RESET BACK TO THE START")
                print("type back to go back")
                directionother = input()

