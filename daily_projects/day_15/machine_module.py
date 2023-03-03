import os
import time
from menu import MENU
from resources_module import update_resources, check_resources

def make_a_drink(drink):
    """
    Makes a drink.

    Args:
    drink (str): The name of the drink to make.

    """

    if check_resources(drink) == False:
        return
    
    if check_founds(drink) == False:
        return
    
    print('Preparing your drink')
    time.sleep(1)
    for i in range(3):
        print("☕ ", end="", flush=True)
        time.sleep(1)
    print(f'\nHere is your {drink}. Enjoy!')
    time.sleep(3)
    os.system('cls')
    return

def check_founds(drink):
    """
    Checks if the user has enough money to buy the specified drink.

    Args:
    drink (str): The name of the drink to buy.

    Returns:
    False if the user does not have enough money.
    True if the user has enough money and any change is returned.

    """
    quarter = int(input('How many quarters? (25c): '))
    dime = int(input('How many dimes? (10c): '))
    nickel = int(input('How many nickels? (5c): '))
    penny = int(input('How many pennies? (1c): '))
    total = quarter * 0.25 + dime * 0.1 + nickel * 0.05 + penny * 0.01
    if total < MENU[drink]['cost']:
        print('Sorry that is not enough money. Money refunded.')
        time.sleep(5)
        os.system('cls')
        return False
    elif total > MENU[drink]['cost']:
        change = round(total - MENU[drink]['cost'], 2)
        print(f'Here is ${change} in change.')
        time.sleep(3)
        os.system('cls')
        return True

def main_menu(drink):
    """
    Displays the main menu and handles user input.

    Args:
    drink (str): The name of the drink selected by the user.

    """
    os.system('cls')

    # coffee machine report - print resources
    if drink == 'report':
        update_resources('report')
        time.sleep(3)
        os.system('cls')
        return
    elif drink == 'supply':
        update_resources()
        time.sleep(3)
        os.system('cls')
        return

    print(f'You chose: {drink}')
    make_a_drink(drink)