from turtle import Turtle, Screen

tim = Turtle()

def draw_square(side_size):
    for side in range(4):
        tim.forward(side_size)
        tim.right(90)
        
def dashed_square(side_size_in_dashes, dash_length):
    for side in range(4):
        dash_line(dash_length, side_size_in_dashes)
        tim.right(90)
        
def dash_line(dash_length, dash_amount):
    for length in range(dash_amount):
        tim.forward(dash_length)
        tim.penup()
        tim.forward(dash_length)
        tim.pendown()

tim.shape('turtle')
tim.color('DarkSlateGray4')

dashed_square(10, 10)

screen = Screen()
screen.exitonclick()