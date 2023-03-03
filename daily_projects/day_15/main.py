import os
import time
from menu import MENU
from resources import resources

def get_resources(drink = ''):
            
    if drink == '':
        return resources
    elif drink in MENU:
        return MENU[drink]['ingredients']
    else:
        print('Invalid drink')
        return False
    
def suppy_resources():
    resources['water'] += int(input('How much water would you like to add? (max 500ml) '))
    resources['milk'] += int(input('How much milk would you like to add? (max 300ml) '))
    resources['coffee'] += int(input('How much coffee would you like to add? (max 200g) '))
    
    if resources['water'] > 500:
        resources['water'] = 500
    if resources['milk'] > 300:
        resources['milk'] = 300
    if resources['coffee'] > 200:
        resources['coffee'] = 200
    return

def check_resources(drink):
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
    print(resources)

def make_a_drink(drink):

    if check_founds(drink) == False:
        return

    if check_resources(drink) == False:
        return
    time.sleep(1)
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
    os.system('cls')
    
    #coffee machine report - print resources
    if drink == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        time.sleep(5)
        os.system('cls')
        return
    elif drink == 'supply':
        suppy_resources()
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        time.sleep(5)
        os.system('cls')
        return
    
    print(f'You chose: {drink}')
    make_a_drink(drink)
    return

def coffee_machine():
    os.system('cls')
    coffee_machine_status = True
    while coffee_machine_status:
        drink = input('What would you like? (espresso/latte/cappuccino): ')
        if drink == 'off':
            break
        else:
            main_menu(drink)
    
coffee_machine()