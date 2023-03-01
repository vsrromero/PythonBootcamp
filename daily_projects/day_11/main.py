import random
import os
from art import logo

# Create a list of cards with the correct values
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
computer_cards = []

game_rolling = True

def deal_card():
    # Use the global variable 'cards' for drawing a card
    return random.choice(cards)

def reset_match():
    global player_cards
    global computer_cards
    player_cards = []
    computer_cards = []
    os.system('cls')

def game_start():
    os.system('cls')
    print(logo)
    global game_rolling
    game_rolling = True
    match()

def continue_playing():
    global game_rolling
    if input('Play again? "Y" or "N" - ').lower() == 'y':
        reset_match()
        return game_start()
    else:
        game_rolling = False
        return 'Thanks for playing!'

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        while score > 21 and 11 in cards:
            cards[cards.index(11)] = 1
            score = sum(cards)
    return score
    
def compare(player_score, computer_score, player_cards, computer_cards):
    global game_rolling

    if player_score == computer_score:
        print(f"Both players have a score of {player_score}. It's a draw.")
    elif player_score > 21:
        print('You went over 21. You lose.')
    elif computer_score > 21:
        print('Dealer went over 21. You win!')
    elif player_score > computer_score:
        print('You win!')
    else:
        print('You lose.')

    print(f'Your final hand: {player_cards}, final score: {player_score}')
    print(f"Dealer's final hand: {computer_cards}, final score: {computer_score}")
    continue_playing()

def match():
    global game_rolling

    player_cards = []
    computer_cards = []

    for i in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(f'Player cards: {player_cards} Total: {calculate_score(player_cards)}')
    print(f'Dealer cards: [{computer_cards[0]}, 🎴]\n')

    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    if player_score == 0:
        print('PLAYER BLACKJACK! YOU WIN!')
        return continue_playing()
    elif computer_score == 0:
        print('DEALER BLACKJACK! YOU LOSE!')
        computer_cards = [10, 11]
        return continue_playing()
    elif computer_score == 21 and len(computer_cards) == 2:
        print('DEALER BLACKJACK! YOU LOSE!')
        return continue_playing()

    while game_rolling:
        if input("Would you like more cards? 'Y' or 'N' - ").lower() == 'y':
            os.system('cls')
            print(logo)
            player_cards.append(deal_card())
            player_score = calculate_score(player_cards)
            print(f'\nPlayer cards: {player_cards} Total: {player_score}')
            print(f'Dealer cards: [{computer_cards[0]}, 🎴]\n')
            if player_score > 21 and 11 in player_cards:
                # Make a copy of the list before modifying it
                temp_cards = player_cards.copy()
                while player_score > 21 and 11 in temp_cards:
                    temp_cards[temp_cards.index(11)] = 1
                    player_score = calculate_score(temp_cards)
                player_cards = temp_cards
            if player_score > 21:
                print(f'BUST! YOU LOSE! your hand is {player_cards} {player_score}')
                game_rolling = False
                return continue_playing()
        else:
            while computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
                os.system('cls')
                print(logo)
                print(f'\nPlayer cards: {player_cards} Total: {player_score}')
                print(f'Dealer cards: {computer_cards} Total: {computer_score}\n')
                if computer_score > 21:
                    print(f"DEALER BUST, YOU WIN!")
                    game_rolling = False
                    return continue_playing()
            compare(player_score, computer_score, player_cards, computer_cards)
            game_rolling = False


game_start()