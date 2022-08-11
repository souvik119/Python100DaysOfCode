## HOUSE RULES
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
from art import logo

def deal_cards():
    """Returns a random card from the cards list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Takes a list as input and returns sum of elements. Also checks for blackjack win condition and removes ace value 11 is sum is greater than 21"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_score(user_score, computer_score):
    """Compares user score vs computer score and declares the winner"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lost, opponent has a blackjack!!"
    elif user_score == 0:
        return "You win! with a BLACKJACK!!!!"
    elif user_score > 21:
        return "You went over 21! You lose"
    elif computer_score > 21:
        return "Oponnent went over 21! You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand:{user_cards} and final score:{user_score}")
    print(f"Computer's final hand:{computer_cards} and final score:{computer_score}")
    print(compare_score(user_score, computer_score))

#Hint:Ask the user if they want to restart the game. If they answer yes, clear the 
#console and start a new game of blackjack and show the logo from art.py.

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()