from turtle import Turtle

class Score(Turtle):
    def __init__(self, x):
        super().__init__()
        self.hideturtle()
        self.up()
        self.score = 0
        self.goto(x, 285)

    def display(self, x):
        self.write(f"Score : {self.score}", False,  x)

    def gameover(self):
        self.up()
        self.goto(0, 0)
        self.write("Game Over ", False, "center")