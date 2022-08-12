# Rules :
# Randomly select a number between 1 and 100
# Make the user guess the number
# 2 levels - easy and hard
# easy has 10 guess attempts
# hard has 5 guess attempts

import random
from art import logo

def generate_target_number():
    """Returns a random integer between 1 and 100"""
    return random.randint(1, 100)

def check_guess(target_number, guess_number):
    """Checks if user guessed number is equal to, greater or lesser than target number"""
    if guess_number == target_number:
        return "equal"
    elif guess_number > target_number:
        return "high"
    else:
        return "low"


def gameplay():
    """Main gameplay function that controls the entire game"""
    print(logo)
    target_number = generate_target_number()
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    if input("Choose a difficulty level. Type 'easy' or 'hard': ") == "easy":
        attempts = 10
    else:
        attempts = 5
    
    continue_game = True
    while continue_game:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        result = check_guess(target_number, guess_number)
        if result == "equal":
            print(f"You go it! The answer was {target_number}.")
            continue_game = False
        elif result == "high":
            print("Too high.")
            if attempts > 1:
                print("Guess again.")
        else:
            print("Too low.")
            if attempts > 1:
                print("Guess again.")

        attempts -= 1
        if attempts < 1:
            continue_game = False
            print("You have run out of guesses, you lose.")

gameplay()