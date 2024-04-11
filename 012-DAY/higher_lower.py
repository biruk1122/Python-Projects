from logo import logo, Vs
from main_data import data
import random
import os

def format_data(account):
    # Takes the account data and returns the printable format.
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    #Use if statment to check if user is correct.
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Display Logo
print(logo)
score = 0
game_should_continue = True

# Generate a random account from the game data.
account_2 = random.choice(data)

# Make the game repetable.
while game_should_continue:
    
    # Making account at position B become the next account at position A.
    account_1 = account_2
    account_2 = random.choice(data)
    while account_1 == account_2:
        account_2 = random.choice(data)

    print(f"Compare A: {format_data(account_1)}.")
    print(Vs)
    print(f"Against B: {format_data(account_2)}.")

    # Ask user for a guess.
    guess = input("Who has more follower? Type 'A' or 'B' ").lower()

    # Check if user is correct.
    # Get follower count of each account.
    a_follower_count = account_1["follower_count"]
    b_follower_count = account_2["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)


    # Clear the screen between rounds.
    os.system('cls')
    print(logo)

    # Give user feedback on their guess.
    # Score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final Score: {score}.")
    