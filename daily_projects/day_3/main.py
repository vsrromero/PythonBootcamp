print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = ''

print('Your ship has just docked on Treasure Island, you need to choose the right path so that you find the treasure on this island full of traps.')

direction = input("You see two possible paths, one following to the right and one to the left, which one do you choose? Left or right?").lower()

if direction == 'left':
    print('A rhinoceros attacked you with no defense chances, Game over!')
elif direction == 'right':
    direction = input('You enter the jungle, and see a bridge that crosses a calm river, which way do you choose to cross? Bridge or river?').lower()
    if direction == 'bridge':
        direction = input('As soon as you cross the bridge, you see two stone doors, one with a symbol of a circle and one with a symbol of a square, which door do you choose? Square or circle?').lower()
        if direction == 'circle':
            print('You found a room full of spears that attacks you. You are dead, game over!')
        else:
            print('You found the treasure! Well done')
    else:
        print("A crocodile was hungry and you're the meal. Game over!")
