from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    # Creating the initial snake.
    def __init__(self, color="white", initial_length=3, initial_direction=0, thickness=20, step=20):
        self.snake = []
        self.steps = 0
        self.alive = True
        self.snake_position = []
        self.step = step
        for i in range(initial_length):
            new_segment = Turtle(shape="square")
            new_segment.color(color)
            new_segment.penup()
            new_segment.goto(- thickness * i, 0)
            self.snake.append(new_segment)
        self.head = self.snake[0]
        self.head.setheading(initial_direction)

    # Defining functions for snake movements and enabling listening to game events.
    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_forward(self):
        # Let us get the current position lists of the segments, from first to last:
        self.snake_position = []
        for segment in self.snake:
            self.snake_position.append(segment.position())
        # Setting the first segment to move.
        self.head.forward(self.step)
        # Now, other segments are repositioned to meet the locations of preceding segments.
        for i in range(1, len(self.snake)):
            self.snake[i].setposition(self.snake_position[i - 1])
        self.steps += 1
        if self.steps == 30: self.alive = False

    def grow_segment(self):
        self.snake.append(self.snake[len(self.snake) - 1].clone())
