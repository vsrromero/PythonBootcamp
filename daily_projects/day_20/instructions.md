# Snake Game

## Steps:

* Create the screen game
    * 600 x 600
* Create the snake body
* Move the snake
* Control the snake using the keyboard
* Detect collision with food
    * Increase the snake length
* Create a scoreboard
* Detect collision with wall
    * Shows game over and the snake stop moving
* Detect collision with tail
    * Shows game over and the snake stop moving


## Documentation:

### Screen update

`screen.tracer(0)` is a method call that disables the automatic updating of the screen during a turtle graphics program. When this method is called with a value of 0, it turns off the animation of the screen, which means that any changes made to the graphics on the screen will not be shown until the screen.update() method is called explicitly.  

~~~
while game_is_on:
    screen.update()
    time.sleep(0.1)
~~~

`screen.update()` is called at the end of each game loop iteration (snake movement) to display the updated graphics on the screen.
`time.sleep(0.1)` wait 0.1 seconds till the next snake movement.

### Snake movement
~~~
for segment in range(len(snake) -1, 0, -1):
    new_x = snake[segment - 1].xcor()
    new_y = snake[segment - 1].ycor()
    snake[segment].goto(new_x, new_y)
snake[0].forward(20)
~~~
This loop updates the positions of each segment of the snake's body. It starts from the second-to-last segment and iterates through each segment towards the head of the snake. For each segment, it retrieves the x and y coordinates of the previous segment and stores them in new_x and new_y. Then, it moves the current segment to the new coordinates using the .goto() method.

After iterating through all the segments, the loop moves the head of the snake (at index 0) forward by 20 units using the .forward() method. This updates the position of the snake's head and starts a new "step" of movement for the snake.

### Snake turning
~~~
def up(self):
    if self.snake_head.heading() != DOWN:
        self.snake_head.setheading(UP)
    return
~~~

Turn snake head to desired direction, except for opposite direction.
E.g. the snake cant move left if it is moving right.
