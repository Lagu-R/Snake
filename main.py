from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
# variable for Turtle and Screen , from turtle module
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
# snake object from snake module
snake  = Snake()
screen.listen()
food = Food()
scoreboard = Scoreboard()
# set direction of snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




# game logic 
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # distance between score and snake
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend()
    
    # detect collision with wall.
    if (snake.head.xcor() > 280 or 
        snake.head.xcor() < -280 or 
        snake.head.ycor() > 280 or 
        snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()

    # detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()







screen.exitonclick()