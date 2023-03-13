from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(0,0,1)
        self.speed("fastest")
        self.spawn_food()

    def spawn_food(self):
        """
        Spawn a food at a random place between -280, 280 x and y position
        The reason that is (-14, 14) * 20 is to food spawn in 20 multiples
        so it places the food in a more centralized place to the snake's body
        """
        random_x = random.randint(-14, 14) * 20
        random_y = random.randint(-14, 14) * 20
        self.goto(random_x, random_y)
