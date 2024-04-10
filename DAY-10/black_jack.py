""" Blackjack Project
Create a deal_card() function that uses the list below to return a random card.
11 is the ace."""

import random
import os
from logo_blackjack import logo


#Returns a random card from the deck.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

""" Create a function called calculate_score() that takes a list of cards as input and return the score.
Take a list of cards and return the score calculated from the cards."""

def calculate_score(cards): 
    """ Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
        and return 0 insread of the actual score. 0 will represent a blackjack in our game."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    """ Inside calculate_score() check for an 11 (ace). if the score is already over 21,
     remove the 11 and replace it with a 1. """
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


""" Create a function called compare() and pass in the user_score and computer_score.
    if the computer and user both have the same score, then it's a draw. if the
    the computer has a blackjack (0), then the user loses. if the user has a blackjack (0),
    then the user wins. if the user_score is over 21, then the user loses. if the computer_score
    is over 21, then the computer loses.  """
    

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "you went over. you lose"
    elif computer_score > 21:
        return "Opponent went over. you win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"

def play_game():
    
    print(logo)
# Deal the user and computer 2 cards each using deal_card().
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    """The Score will need to be rechecked with every new card drawn and the checks in the
           Hint-3 need to be repeated until the game ends."""

    while not is_game_over: 

        """Call the Calculate_score(). If the computer or the user has a blackjack (0)
           or if the user's score is over 21, then the game over."""

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    your cards: {user_cards}, current score: {user_score}")
        print(f"    computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        

            """ Hint-3: If the game is not over, ask the user if they want to draw another card. If yes,
            then use the deal_card() function to add another card to the user_cards list.
            if no, then the game has over."""
            
        else:
            user_can_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_can_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    """ Once the user is done. it's time to let the computer play. The computer should keep
        drawing cards as long as it has a score less than 17."""

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score)) 

    """ Ask the user if they want to restart the game. if they answer yes, clear the console and
       start a new game of blackjack and show the logo from log_blackjack.py"""

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    os.system('cls')
    play_game()
