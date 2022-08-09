from concurrent.futures.process import _threads_wakeups
import os
from art import logo

auction_dict = {}

def auction_record():
    user_name = input("What is your name?")
    user_bid = int(input("What's your bid? $"))
    auction_dict[user_name] = user_bid

def declare_winner():
    winning_bid = 0
    for bidder in auction_dict:
        if auction_dict[bidder] > winning_bid:
            winning_bid = auction_dict[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${winning_bid}.")

def gameplay():
    print(logo)
    print("Welcome to the secret auction program.")
    continue_game = True
    while continue_game:
        auction_record()
        user_input_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if user_input_continue == "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            declare_winner()
            print("Thanks for the bid!!")
            continue_game = False

if __name__ == '__main__':
    gameplay()