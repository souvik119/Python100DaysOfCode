import random

#ascii art for rock, paper and scissors
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

#getting user input
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.  "))
if user_input == 0:
    user_input = rock
elif user_input == 1:
    user_input = paper
else:
    user_input = scissors
print(user_input)

#getting random computer input making sure there is no draw
computer = [rock, paper, scissors]
computer.remove(user_input)
computer_input = random.choice(computer)
print(f"Computer chose:{computer_input}")

#game decision making
if user_input == rock:
    if computer_input == scissors:
        print("You win")
    else:
        print("You lose")
elif user_input == paper:
    if computer_input == rock:
        print("You win")
    else:
        print("You lose")
else:
    if computer_input == paper:
        print("You win")
    else:
        print("You lose")
