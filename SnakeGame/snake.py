# The overall use of this module is that we can manage all the complexities related to our snake in a different section.
from turtle import Turtle
# These are some constant values which can be changed in our program without actually changing much in our program.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Here we create a "Snake" class in the module "snake.py
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
# This function is used tp create the default segment(length) of the body of the snake.

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
# This function is going to add a new segment to our snake. i.e. make our snake longer.

    def add_segment(self, position):
        new_segment = Turtle("circle")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
# this function is going to call the "extend" function whenever the snake eats food, therefore extending our snake

    def extend(self):
        self.add_segment(self.segments[-1].position())
# This function defines the movement of our snake. basic concept used here is that the entire body should follow the
# the movement of the head.

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
# This function checks the basic rules of snake game. i.e. the snake cannot trace itself back.

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
