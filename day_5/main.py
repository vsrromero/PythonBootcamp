#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) #52
nr_symbols = int(input(f"How many symbols would you like?\n")) #9
nr_numbers = int(input(f"How many numbers would you like?\n")) #10

easy_pass = ''
password = ''

#get a random position from the lists and append to the variables according the chosen option
for i in range(int(nr_letters)):
    easy_pass = easy_pass + letters[random.randint(0, len(letters)-1)]
    password = password + letters[random.randint(0, len(letters)-1)]
for i in range(int(nr_symbols)):
    easy_pass = easy_pass + symbols[random.randint(0, len(symbols)-1)]
    password = password + symbols[random.randint(0, len(symbols)-1)]
for i in range(int(nr_numbers)):
    easy_pass = easy_pass + numbers[random.randint(0, len(numbers)-1)]
    password = password + numbers[random.randint(0, len(numbers)-1)]

password = list(password) #converts the string into a list/array
random.shuffle(password) #shuffles the list
password = "".join(password) #convert the list into a string

print(easy_pass)
print(password)