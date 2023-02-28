from art import logo
import random
import os

tries_remaining = 0

def game_level(level):
    global tries_remaining
    if level == 'hard':
        tries_remaining = 5
    else:
        tries_remaining = 10

def number_guessing():
    global tries_remaining
    number_to_guess = random.randint(1,100)
    while tries_remaining > 0:
        user_try = int(input("Make a guess: "))
        if user_try == number_to_guess:
            os.system('cls')
            print(logo)
            print(f'Congratulations! You guessed the number {number_to_guess} with {tries_remaining} tries remaining.')
            if input('Would you like to play again? "yes" or "no"').lower() == 'yes':
                game_start()
                number_guessing()
            return
        elif number_to_guess > user_try:
            os.system('cls')
            print(logo)
            print('Too low.')
        else:
            os.system('cls')
            print(logo)
            print('Too high.')
        tries_remaining -= 1
        print(f'you have {tries_remaining} tries remaining')

    os.system('cls')
    print(logo)
    print('You have no more tries')
    print(f'Sorry, you did not guess the number. The number was {number_to_guess}.')
    if input('Would you like to play again? "yes" or "no"').lower() == 'yes':
        game_start()
        number_guessing()

def game_start():
    os.system('cls')
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100")
    level = input('Choose a difficulty. Type "easy" or "hard": ')
    game_level(level)
    print(f'you have {tries_remaining} tries remaining')
    
game_start()
number_guessing()