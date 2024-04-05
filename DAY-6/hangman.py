#Hangman Project

import random

# step-1: Randomly choose a word from the word_list and
# assign it to a variable called chosen_word.
# - Create an empty list called display.
# - so if the choosen_word was "apple", display should be
# ["-", "-", "-", "-", "-"] with 5 "-" representing
# each letter to guess.
# - Use a while loop to let the user guess again.The
# loop should only stop once the user has gussed all
# the letters in the chosen_word and 'display' has no
# more blanks("-"). Then you can tell the user you won.

#Create a blanks


# step-2: Ask the user to guess a letter and assign
# their answer to a variable called guess. make guess
# lower case.
# - Loop through each position in the chosen_word
# - if the letter at that position maches 'guess' then
# reveal that letter in the display at that position.
# e.g, If the user guessed "p" and chosen_word was
# "apple", then display should be ["-", "p", "-", "-", "-"].

#word_list = ["ardvark", "baboon", "camel"]
from hangman_word_list import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# Create a variable called 'lives' to keep track of
# the number of lives left.
# Set 'lives' to equal 6.
end_of_game = False
lives = 6
# Import logo from signs.py and print it at the start
# ot the game
from signs import logo
print(logo)
# Testing code
#print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []

for _ in range(word_length):
    display += "_"
     

while not end_of_game:
    guess = input("Guess a letter: ").lower()
# step-3 : Check if the letter the user guessed is
# one of the letter in the chosen_word.
# If the user has entered a letter they've already
# guessed, print the letter and left them know
    if guess in display:
        print(f"You've already guessed {guess}")

#Check guessed letters
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current Position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
          

# If guess is not a letter in the chosen_word
# Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and
# it should print "you lose"
            
    if guess not in chosen_word:
# If the letter is not in the chosen_word print out the
# letter and let them know it's in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
# Join all the elements in the list and turn it into a string.
    print(f"{' '.join(display)}")

#Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You Win.")

# Print the ASCII art from 'stages' that corresponds to
# the current number of 'lives' the user has remaining.
    from signs import stages
    print(stages[lives])
