from random_word_request import request_word_by_level as word_by_level
from art import stages, logo

print(logo)

level = int(input('Choose a level:\n1 for words till 5 letters\n2 for words till 8 letters\n3 for words with more than 8 letters\n'))

chosen_word = word_by_level(level)

lives = 6

display = []
chosen_letters = []

display = ["_" for letter in chosen_word]
print(f"{' '.join(display)}")

end_of_game = False

while not end_of_game:
    guess = input('Guess a letter: ').lower()

    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess
            print(stages[lives])
            print(f"{' '.join(display)}")
            print(f'Letters already chosen: {" ".join(chosen_letters)}\n')

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"{' '.join(display)}")
        if guess not in chosen_letters:
            chosen_letters.append(guess)
        print(f'Letters already chosen: {" ".join(chosen_letters)}\n')

        if lives == 0:
            end_of_game = True
            break

    if "_" not in display:
        end_of_game = True

if end_of_game and "_" not in display and lives == 6:
    print("YOU WIN WITH PERFECT SCORE!")
elif end_of_game and "_" not in display:
    print("YOU WIN!")
else:
    print("YOU LOSE!")
    print(f'The word was: {chosen_word}')
