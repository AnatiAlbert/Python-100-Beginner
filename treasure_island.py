print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You've arrived at a crossroad, type 'left' to turn left, or 'right' to turn right.\n").lower()

if choice1 == "left":
    choice2 = input("You've arrived at the lake, will you 'swim' or 'wait'.\n").lower()
    if choice2 == "wait":
        choice3 = input("You've arrived at a house. Choose one of the doors, 'red', 'yellow' or 'blue'?\n").lower()
        if choice3 == "red":
            print("You've entered a room of fire. Game Over.")
        elif choice3 == "yellow":
            print("You win! You've entered the treasure room.")
        elif choice3 == "blue":
            print("You've entered a room full of beasts. Game Over.")
        else:
            print("You've entered the wrong room. Game Over.")
    else:
        print("You were attacked by trout. Game Over.")
else:
    print("You have fallen into a hole, Game Over.")
