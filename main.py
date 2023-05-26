import time
import turtle
from turtle import Turtle,Screen
from snake import Sanke
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title(titlestring="My snake Game")
screen.tracer(0)

# segments=[]
snake = Sanke()
food = Food()
scoreboard = Scoreboard()

# screen.update()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on =True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()
    if (snake.head.xcor() > 280 or snake.head.xcor()<-280 or snake.head.ycor()>280or snake.head.ycor()<-280):
        game_is_on=False
        scoreboard.game_over()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()














screen.exitonclick()
