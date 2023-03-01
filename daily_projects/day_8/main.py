from caesar_cypher import caesar
from art import logo

print(logo)

loop = True
while loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    while direction != 'encode' and direction != 'decode':
        direction = input("Choose a valid option\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction=direction, text=text, shift=shift)
    
    keep_coding = input('Would you like to keep cyphering?\nY or N\n').lower()

    if keep_coding != 'y':
        print("Bye!")
        loop = False