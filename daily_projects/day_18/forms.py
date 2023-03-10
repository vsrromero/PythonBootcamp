from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

def draw_shapes(max_sides):
    for sides in range(3, max_sides+1):
        pen_color = (random.random(), random.random(), random.random())
        timmy.pencolor(pen_color)

        angle = 360 / sides
        for j in range(sides):
            timmy.forward(100)
            timmy.right(angle)

draw_shapes(5)
    
screen.exitonclick()
