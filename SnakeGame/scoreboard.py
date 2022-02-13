# This module manages our scoreboard. i.e it counts our score.
from turtle import Turtle
ALIGN = "center"
# Choosing font, (as a designer, Helvetica is my favourite font :D)
FONT = ("helvetica", 24, "normal")
# A Class named "Scoreboard" was created.


class ScoreBoard(Turtle):
    # Some default methods that are pre-associated with our scoreboard.

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"SCORE : {self.score} ", align=ALIGN, font=FONT)
        self.penup()
    # since we are using our turtle to write, so we need to remove previous written data and replace it by new.

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE : {self.score} ", align=ALIGN, font=FONT)
    # This function is called in case our game is over, i.e. either snake bit itself or hit the wall.

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write("GAME OVER", align="center", font=FONT)