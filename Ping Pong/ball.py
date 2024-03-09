from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.shape("square")
        self.shapesize(.8, .8)
        self.goto(0, 100)
        self.showturtle()
        self.xmove = 5
        self.n = 1
        self.ymove = 5

    def move(self):
        y = self.ycor()
        x = self. xcor()
        self.goto(x+self.xmove, y+self.ymove)

    def bounce(self):
        self.ymove *= -1

    def refersh(self):
        self.speed(1)
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        self.xmove = 5
        self.ymove = 5

    def sidebounce(self):
        self.xmove *= -1

    def speedup(self):
        if self.n < 10:
            return self.n+1
        else:
            return 0
