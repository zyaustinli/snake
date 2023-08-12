from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title('Snake game')
screen.tracer(0)


snake = Snake()

food = Food()
scoreboard = Scoreboard()



screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor() >280 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for seg in snake.segments[1:]:
        
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()


    

screen.exitonclick()