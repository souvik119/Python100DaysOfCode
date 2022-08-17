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

#Hint:Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, 
#then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. 
#If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, 
#then the player with the highest score wins.
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

user_cards = []
computer_cards = []
is_game_over = False

#_ because we do not need a variable
for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

while not is_game_over:
    #Hint:Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    #Hint:If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add 
    #another card to the user_cards List. If no, then the game has ended.
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_cards())
        else:
            is_game_over = True

#Hint:Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17
#0 is blackjack so just less than 17 condition will not work
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_cards())
    computer_score = calculate_score(computer_cards)

print(f"Your final hand:{user_cards} and final score:{user_score}")
print(f"Computer's final hand:{computer_cards} and final score:{computer_score}")
print(compare_score(user_score, computer_score))