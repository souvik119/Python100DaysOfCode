import random
from hangman_words import word_list
from hangman_art import stages, logo
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(word_list)

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Depict chosen word as blank and fill it as user guesses each letter
display = ["_"]*len(chosen_word)

lives = 6

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}")

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    
    if guess not in chosen_word:
        print(f"{guess} is not chosen word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])