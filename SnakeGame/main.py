# Our main manages all the other classes that we created for managing our snake game.
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
# Time module plays a big role in making our game more beautiful.
import time

# Creating a screen using screen class using turtle module.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("olive")
screen.title("My Snake Game")
screen.tracer(0)

# Here we make our snake object that has some previous attributes.
snake = Snake()
# food object created and spawned in a random location.
food = Food()
# Scoreboard object created and set its initial value to 0.
scoreboard = ScoreBoard()

# Listen is a screen method that checks for users input, very important for controlling our snake.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# while loop will run until the program is terminated which is possible only in two cases. either snake bit itself or
# hit the boundary of the screen.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # when distance between snake head and food is less than 15, then the snake extends its length and scoreboard is
    # refreshed.
    if snake.head.distance(food) < 15:
        food.random_location()
        scoreboard.refresh()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()