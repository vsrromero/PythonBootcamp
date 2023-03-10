from turtle import Turtle, Screen
import random

timmy = Turtle()
radius = 100
timmy.speed(0)

def random_color():
    color = [random.random(), random.random(), random.random()]
    return color

def spirograph(gap_size):
    for c in range(int(360 / gap_size)):
        timmy.color(random_color())
        timmy.circle(radius)
        timmy.setheading(timmy.heading() + gap_size)
        
spirograph(5)

screen = Screen()
screen.exitonclick()