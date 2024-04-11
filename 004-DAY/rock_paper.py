"""Rock Paper Scissors Project"""

import random

rock = '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''

   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

images = [rock, paper, scissors]
user_choice = int(input("What Do You Choose? Type 0 For Rock, 1 For Paper and 2 For Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print ("You Typed An Invalid Number, You Lose!")
else:
    print(images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer Choose: ")
    print(images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice > user_choice:
        print("You Lose.")
    elif user_choice > computer_choice:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose.")
    elif computer_choice == user_choice:
        print("It's a Draw.")