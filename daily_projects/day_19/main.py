from turtle import Turtle, Screen
import random

is_race_on = False

all_turtles = []

turtle_colors = ['purple', 'red', 'orange', 'yellow', 'green', 'blue']

screen = Screen()

screen_size = None

while screen_size is None:
    try:
        screen_size_input = screen.textinput(title='Choose your racing size', prompt='Choose between 500 and 900')
        screen_size = int(screen_size_input)

        if screen_size < 500 or screen_size > 900:
            print("Invalid choice! Please choose a number between 500 and 900.")
            screen_size = None

    except ValueError:
        print("Invalid input! Please enter a valid number.")

screen.setup(width=screen_size, height=400)

x_axis = ((screen.window_width() / 2) * -1) + 10
y_axis = -60

finish_line = int((screen.window_width() / 2) - (40/2))

user_choice = screen.textinput(title='Place your bet.', prompt='Choose a color red/blue/green/purple/yellow/orange:')

while not user_choice in turtle_colors:
    user_choice = screen.textinput(title='Place your bet.', prompt='Choose a color red/blue/green/purple/yellow/orange:')

for turtle in range(0, 6):
    color = turtle_colors[turtle]
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape('turtle')
    new_turtle.color(color)
    new_turtle.speed(8)
    new_turtle.goto(x=x_axis, y=y_axis)
    new_turtle.speed(6)
    y_axis += 30
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > finish_line:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f'You won with the color {winning_color}')
            else:
                print(f'You lost, the winning color is {winning_color}')
            break
        random_turtle_distance1 = random.randint(0, 10)
        random_turtle_distance2 = random.randint(0, 5)
        random_turtle_distance3 = random.randint(2, 10)
        turtle.forward(random_turtle_distance1)
        turtle.forward(random_turtle_distance2)
        turtle.forward(random_turtle_distance3)

screen.exitonclick()