from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("data.txt", "r") as file:
            self.hs = file.read()
        self.highscore = int(self.hs)
        self.goto(0, 280)
        self.color("white")

    def display(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highscore}", False,  "center")

    def scoreup(self):
        self.score += 1
        return self.score

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.hs = str(self.highscore)
            with open("data.txt", "w") as file:
                file.write(self.hs)

        self.score = 0
        self.display()
