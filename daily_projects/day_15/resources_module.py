import os
import time
from menu import MENU
from resources import resources

# Define constants for max values
MAX_WATER = 500   # ml
MAX_MILK = 300   # ml
MAX_COFFEE = 200  # g

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

    if resources['water'] > MAX_WATER:
        resources['water'] = MAX_WATER
    if resources['milk'] > MAX_MILK:
        resources['milk'] = MAX_MILK
    if resources['coffee'] > MAX_COFFEE:
        resources['coffee'] = MAX_COFFEE

    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')

def deduct_resources(drink):
    """
    Deducts the ingredients of a drink from the resources.
    
    Args:
        drink (str): The drink to be deducted from the resources.

    """
    drink_ingredients = get_resources(drink)
    resources_available = get_resources()
    for ingredient in drink_ingredients:
        resources_available[ingredient] -= drink_ingredients[ingredient]

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
            time.sleep(3)
            os.system('cls')
            return False
    #if all resources are available, deduct resources
    deduct_resources(drink)