import os
import time
from menu import MENU
from resources import resources

def get_resources(drink = ''):
    """
    Returns the resources available in the machine.

    Args:
    drink (str): The name of the drink to get ingredients for. Defaults to ''.

    Returns:
    A dictionary of the form {'water': int, 'milk': int, 'coffee': int} if drink is ''.
    A dictionary of the form {'water': int, 'milk': int, 'coffee': int} for the specified drink if it is in MENU.
    False otherwise.

    """
            
    if drink == '':
        return resources
    elif drink in MENU:
        return MENU[drink]['ingredients']
    else:
        print('Invalid drink')
        return False
    
def update_resources(report = ''):
    """
    Updates the resources available in the machine.

    Args:
    report (str): If 'report', prints a report of the current resources. Defaults to ''.

    """
    
    if report == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        return
    
    resources['water'] += int(input('How much water would you like to add? (max 500ml) '))
    resources['milk'] += int(input('How much milk would you like to add? (max 300ml) '))
    resources['coffee'] += int(input('How much coffee would you like to add? (max 200g) '))

    if resources['water'] > 500:
        resources['water'] = 500
    if resources['milk'] > 300:
        resources['milk'] = 300
    if resources['coffee'] > 200:
        resources['coffee'] = 200

    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')

def check_resources(drink):
    """
    Checks if there are enough resources to make the specified drink.

    Args:
    drink (str): The name of the drink to make.

    Returns:
    False if there are not enough resources to make the drink.
    None otherwise.

    """
    drink_ingredients = get_resources(drink)
    resources_available = get_resources()
    #check if all resources are available
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources_available[ingredient]:
            print(f'Sorry there is not enough {ingredient}')
            time.sleep(5)
            os.system('cls')
            return False
    #if all resources are available, deduct resources
    for ingredient in drink_ingredients:
        resources_available[ingredient] -= drink_ingredients[ingredient]

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
        time.sleep(5)
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
        time.sleep(5)
        os.system('cls')
        return
    elif drink == 'supply':
        update_resources()
        time.sleep(5)
        os.system('cls')
        return

    print(f'You chose: {drink}')
    make_a_drink(drink)

def coffee_machine():
    """
    The main function that runs the coffee machine.

    """
    os.system('cls')
    coffee_machine_status = True
    while coffee_machine_status:
        drink = input('What would you like? (espresso/latte/cappuccino): ')
        if drink == 'off':
            break
        else:
            main_menu(drink)
    
coffee_machine()