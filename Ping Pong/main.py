from paddle import Paddle
from turtle import Screen
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(600, 600)
paddle = Paddle(-292)
paddle2 = Paddle(287)
ball = Ball()
score1 = Score(-150)
score2 = Score(150)

screen.listen()
screen.onkeypress(paddle.up, "w")
screen.onkeypress(paddle.down, "s")
screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")
dist = [8, 28, 28]
gameon = True
while gameon:
    ball.move()
    score1.display("left")
    score2.display("right")

    if ball.distance(paddle) < 51 and ball.xcor() < -282:
        ball.sidebounce()
        score1.score += 1
        score1.clear()
        ball.speed(ball.speedup())

    if ball.distance(paddle2) < 51 and ball.xcor() > 277:
        ball.sidebounce()
        score2.score += 1
        score2.clear()
        ball.speed(ball.speedup())

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()

    if ball.xcor() > 300 or ball.xcor() < -300:
        ball.refersh()

    if score1.score > 9 or score2.score > 9:
        score1.gameover()
        gameon = False

screen.exitonclick()
