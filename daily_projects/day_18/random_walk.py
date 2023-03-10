from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.pensize(4)

timmy.speed(0)

angles = [0, 90, 180]
directions = [lambda angle: timmy.right(angle), lambda angle: timmy.left(angle)]

def move():
    timmy.forward(30)
    random.choice(directions)(random.choice(angles))

def random_walk(movements):
    for walk in range(movements):
        color = [random.random(), random.random(), random.random()]
        timmy.pencolor(color)
        move()
    

random_walk(200)

screen = Screen()
screen.exitonclick()

