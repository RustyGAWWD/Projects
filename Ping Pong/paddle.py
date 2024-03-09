from turtle import Turtle
class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.hideturtle()
        self.speed(3)
        self.shape("square")
        self.shapesize(1, 5)
        self.penup()
        self.goto(x, 0)
        self.setheading(90)
        self.showturtle()


    def up(self):
            if self.ycor() < 292:
                self.forward(10)

    def down(self):
            if self.ycor() > -292:
                self.backward(10)





