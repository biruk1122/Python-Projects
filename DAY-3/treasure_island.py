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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome To Treasure Island")
print("Your Mission is To Find The Treasure.")
way1 = input("You're At a Crossroad, Where Do You Go? Type 'Left' or 'Right'.\n")
if way1 == "left":
    way2 = input("You've Come to Lake. There is an Island in the Middle of the Lake. Type 'Wait' to wait for a Boat. "
                 "Type 'Swim' to swim Across\n").lower()
    if way2 == "wait":
        way3 = input("You Arrive at the Island Unharmed. There is a House with 3 Doors. One Red, Yellow and Blue. "
                     "Which Color Do You Choose?\n").lower()
        if way3 == "red":
            print("It's a Room Full of Fire. Game Over.")
        elif way3 == "yellow":
            print("You Found the Treasure! You Win!")
        elif way3 == "blue":
            print("You Enter A Room of Full of Water. Game Over.")
        else:
            print("You Choose A Door that Doesn't Exist. Game Over.")
    else:
        print("You got Attacked by Angry Trout. Game Over.")
else:
    print("You Fell into A Hole. Game Over.")
    