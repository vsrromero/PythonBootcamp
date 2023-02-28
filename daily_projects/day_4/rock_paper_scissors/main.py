import random
import game_aux

player_choice = int(input('"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."\n'))

computer_choice = random.randint(0,2)

if player_choice > 2 or player_choice < 0:
    print('Choose a valid option, You lose!')

elif computer_choice == player_choice:
    if computer_choice == 0:
        print(f'Computer choice is Rock\n {game_aux.rock}\n')
    elif computer_choice == 1:
        print(f'Computer choice is Paper\n {game_aux.paper}\n')
    else:
        print(f'Computer choice is Scissors\n {game_aux.scissors}\n')

    if player_choice == 0:
        print(f'Your choice is Rock\n {game_aux.rock}\n')
    elif player_choice == 1:
        print(f'Your choice is Paper\n {game_aux.paper}\n')
    elif player_choice == 2:
        print(f'Your choice is Scissors\n {game_aux.scissors}\n')

    print('It is a draw\n')


elif computer_choice == 0 and player_choice == 1:
    print(f'Computer choice is Rock\n {game_aux.rock}\n')
    print(f'Your choice is Paper\n {game_aux.paper}\n')
    print('You win\n')
elif computer_choice == 0 and player_choice == 2:
    print(f'Computer choice is Rock\n {game_aux.rock}\n')
    print(f'Your choice is Scissors\n {game_aux.scissors}\n')
    print('You lose\n')
elif computer_choice == 1 and player_choice == 0:
    print(f'Computer choice is Paper\n {game_aux.paper}\n')
    print(f'Your choice is Rock\n {game_aux.rock}\n')
    print('You lose\n')
elif computer_choice == 1 and player_choice == 2:
    print(f'Computer choice is Paper\n {game_aux.paper}\n')
    print(f'Your choice is Scissors\n {game_aux.scissors}\n')
    print('You win\n')
elif computer_choice == 2 and player_choice == 0:
    print(f'Computer choice is Scissors\n {game_aux.scissors}\n')
    print(f'Your choice is Rock\n {game_aux.rock}\n')
    print('You win\n')
elif computer_choice == 2 and player_choice == 1:
    print(f'Computer choice is Scissors\n {game_aux.scissors}\n')
    print(f'Your choice is Paper\n {game_aux.paper}\n')
    print('You lose\n')