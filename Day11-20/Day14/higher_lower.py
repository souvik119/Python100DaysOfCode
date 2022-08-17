# Higher Lower game is a comparison between 2 different instagram accounts about which one has higher followers
# There are 2 choices provided: A and B (both randomly chosen from a list) and the player has to guess which account has more followers A or B
# If the player chooses correctly then B becomes A for the next round and B is choosen randomly from the list again and the score increases by 1
# If the player chooses incorrectly then game ends and the final score is displayed

# List of accounts is defined as followed
# each item is a dictianry with the following keys:
# name
# follower_count
# description
# country

import os
import random
from game_data import data
from art import logo, vs

def print_gameplay(A, B):
    """Formats and prints gameplay message between A and B"""
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")


def compare_followers(A, B):
    """Asks user for input and compares whether A or B has more followers and returns True if user chooses correctly"""
    user_input = input("Who has more followers? Type 'A' or 'B': ")
    if user_input == 'A' and A["follower_count"] >= B["follower_count"]:
        return True
    elif user_input == 'B' and B["follower_count"] >= A["follower_count"]:
        return True
    else:
        return False


def gameplay():
    """Main function that controls other functions"""
    continue_game = True
    score = 0
    #randomly choose 2 items from list as A and B
    A = random.choice(data)
    B = random.choice(data)
    if A == B:
        B = random.choice(data)
    print(logo)
    print_gameplay(A, B)
    continue_game = compare_followers(A, B)

    while continue_game:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        if continue_game:
            A = B
            B = random.choice(data)
            if A == B:
                B = random.choice(data)
            score += 1
            print(f"You are right! Current Score: {score}")
        else:
            break
        print_gameplay(A, B)
        continue_game = compare_followers(A, B)
    
    print(f"Sorry that is wrong. Final Score: {score}")


gameplay()