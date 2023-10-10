from sanke import Snake
from food import Food
import time
from turtle import  Screen
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
score.display()

screen.listen()
screen.onkey(snake.moveforward, "Up")
screen.onkey(snake.moveback, "Down")
screen.onkey(snake.moveleft, "Left")
screen.onkey(snake.moveright, "Right")

gameon = True
while gameon:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.tom[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.scoreup()
        score.display()

    if snake.tom[0].xcor() > 290 or snake.tom[0].xcor() < -290 or snake.tom[0].ycor() > 290 or snake.tom[0].ycor() < -290:
        score.reset()
        snake.reset()

    a = snake.tom[1:len(snake.tom)]

    for i in a:

        if snake.tom[0].distance(i) < 10:
            score.reset()


screen.exitonclick()