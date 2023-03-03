import os
from menu import MENU
from machine_module import main_menu

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