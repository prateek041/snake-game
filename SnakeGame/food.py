# Use of this module is to create food on random locations throughout the screen.
from turtle import Turtle
import random

# Here we create class "Food"
# Our Food class is importing all the methods and properties from the "Turtle" module being is "super" or "parent" class
# which simply follows the concept of "inheritance"


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("pink")
# By using random module we can make our food spawn on random locations throughout our game.

    def random_location(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)