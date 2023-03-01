# Import the required modules and logo
from art import logo
import random
# I am coding in vscode on windows, so I am using os.system('cls') when I want to clear my prompt
import os

# Define function to determine the number of tries based on the chosen level of difficulty
def game_level(level):
    if level == 'hard':
        return 5
    else:
        return 10

# Define function to play the number guessing game
def number_guessing(level):
    # Initialize number of tries based on the chosen level of difficulty
    tries_remaining = game_level(level)
    # Generate a random number between 1 and 100 for the user to guess
    number_to_guess = random.randint(1,100)
    # Loop until the user runs out of tries or guesses the correct number
    while tries_remaining > 0:
        # Prompt the user to make a guess and convert the input to an integer
        user_try = int(input("Make a guess: "))
        # If the user guesses the correct number, display a message and ask if they want to play again
        if user_try == number_to_guess:
            os.system('cls')
            print(logo)
            print(f'Congratulations! You guessed the number {number_to_guess} with {tries_remaining} tries remaining.')
            if input('Would you like to play again? "yes" or "no": ').lower() == 'yes':
                # If the user wants to play again, start a new game and return from the function
                game_start()
                number_guessing(level)
            return
        # If the user's guess is too low, display a message indicating that
        elif number_to_guess > user_try:
            os.system('cls')
            print(logo)
            print('Too low.')
        # If the user's guess is too high, display a message indicating that
        else:
            os.system('cls')
            print(logo)
            print('Too high.')
        # Decrement the number of tries remaining and display the updated count
        tries_remaining -= 1
        print(f'you have {tries_remaining} tries remaining')

    # If the user runs out of tries without guessing the correct number, display a message and ask if they want to play again
    # I am clearing the prompt here so I can keep clean and tidy, I also print the logo again so it remains on screen
    os.system('cls')
    print(logo)
    print('You have no more tries')
    print(f'Sorry, you did not guess the number. The number was {number_to_guess}.')
    if input('Would you like to play again? "yes" or "no": ').lower() == 'yes':
        # If the user wants to play again, start a new game
        game_start()
        number_guessing(level)

# Define function to start a new game
def game_start():
    # Here is where I clear the prompt before starting a game
    os.system('cls')
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100")
    # Prompt the user to choose a difficulty level and display the number of tries they have
    level = input('Choose a difficulty. Type "easy" or "hard": ')
    tries_remaining = game_level(level)
    print(f'you have {tries_remaining} tries remaining')
    # Start a new game
    number_guessing(level)

# Start the first game
game_start()