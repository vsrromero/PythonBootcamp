import os
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))

    for operator in operations:
        print(operator)
    
    should_continue = True
    while should_continue:
        operation_symbol = input("Choose an operation: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_calc = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or type 'e' to exit: ").lower()
        if  continue_calc == 'y':
            num1 = answer
        elif continue_calc == 'e':
            print('Bye')
            break
        else:
            should_continue = False
            os.system('cls')
            calculator()

