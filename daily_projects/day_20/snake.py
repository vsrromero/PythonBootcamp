from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        """Create a new snake with starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake."""
        new_segment = Turtle("square")
        new_segment.color(1,1,1)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extend the snake by adding a new segment to the end."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward by one step."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        """Turn the snake upwards."""
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        """Turn the snake downwards."""
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        """Turn the snake to the left."""
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        """Turn the snake to the right."""
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
