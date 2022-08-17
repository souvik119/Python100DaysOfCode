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

def deal_cards():
    """Returns a random card from the cards list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

user_cards = []
computer_cards = []

#_ because we do not need a variable
for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())


def calculate_score(cards):
    """Takes a list as input and returns sum of elements. Also checks for blackjack win condition and removes ace value 11 is sum is greater than 21"""
    #Hint:Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and 
    #return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #Hint:Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove 
    #the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)