import random
import os
from game_data import data
from art import logo, vs

def get_index(name):
    """Return the index of the person with the given name in the data list."""
    for i, d in enumerate(data):
        if d['name'] == name:
            index = i
            return index

def pick_person():
    """Return a random person from the data list."""
    person = random.choice(data)
    person_name = person['name']
    index = get_index(person_name)
    person_picked = (data[index])
    return person_picked

def new_turn(account_b_name, account_b_followers):
    """Print the logo and the message for a new turn in the game."""
    os.system('cls')
    print(logo)
    print(f'You are right,\n{account_b_name} has {account_b_followers} milions')

def check_followers(account_a_followers, account_b_followers):
    """
    Compare the number of followers of two Instagram accounts and return the letter 'a' or 'b'
    depending on which account has more followers.
    """
    return 'a' if account_a_followers > account_b_followers else 'b'
    
def game_start():
    """Start the game."""
    play_again = True
    while play_again:
        os.system('cls')
        print(logo)
        print('Guess who has more followers on Instagram.')
        score = 0
        right_choice = True
        account_a = pick_person()
        while right_choice:
            account_b = pick_person()
            while account_b == account_a:
                account_b = pick_person()
            print(f"Instagram account A: {account_a['name']}, {account_a['description']}, from {account_a['country']}.")
            print(vs)
            print(f"Instagram account B: {account_b['name']}, {account_b['description']}, from {account_b['country']}.")
            choice = input('Who has more followers? Type "A" or "B": ').lower()
            if choice == check_followers(account_a['follower_count'], account_b['follower_count']):
                new_turn(account_b['name'], account_b['follower_count'])
                account_a = account_b
                score += 1
            else:
                print(f"You are wrong: {account_a['name']} has {account_a['follower_count']} milions\nAnd {account_b['name']} has {account_b['follower_count']} milions")
                print(f'Your score is {score}')
                right_choice = False
                if input('Would you like to play again? Type "Y" or "N": ').lower() == 'y':
                    break
                else:
                    play_again = False

game_start()