import random
import requests

endpoint = 'https://random-word-api.herokuapp.com/word?length='

def request_word_by_level(level):
    if level == 1:
        letters = random.randint(3, 5)
        response = requests.get(f'{endpoint}{letters}')
        chosen_word = response.json()[0]
        return chosen_word
    
    elif level == 2:
        letters = random.randint(6, 8)
        response = requests.get(f'{endpoint}{letters}')
        chosen_word = response.json()[0]
        return chosen_word
    else:
        letters = random.randint(9, 15)
        response = requests.get(f'{endpoint}{letters}')
        chosen_word = response.json()[0]
        return chosen_word


#* The api is returning a list, so the first and only item from the list is passed to the variable using response.json()[0]

