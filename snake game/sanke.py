from turtle import Turtle
positions = [(0.00, 0.00), (-20.00, 0.00), (-40.00, 0.00)]


class Snake:

    def __init__(self):
        self.tom = []
        self.createsnake()

    def createsnake(self):
        for i in positions:
            self.add(i)


    def add(self,positions):
        tim = Turtle("square")
        tim.up()
        tim.color("white")
        tim.goto(positions)
        self.tom.append(tim)


    def extend(self):
        self.add(self.tom[-1].pos())
        self.add(self.tom[-1].pos())
        self.add(self.tom[-1].pos())

    def move(self):
        for i in range(len(self.tom)-1, 0, -1):
            pos = self.tom[i - 1].pos()
            self.tom[i].goto(pos)
        self.tom[0].forward(10)


    def moveleft(self):
        if self.tom[0].heading() != 0:
            self.tom[0].setheading(180)

    def moveright(self):
        if self.tom[0].heading() != 180:
            self.tom[0].setheading(0)

    def moveforward(self):
        if self.tom[0].heading() != 270:
            self.tom[0].setheading(90)

    def moveback(self):
        if self.tom[0].heading() != 90:
            self.tom[0].setheading(270)
    def pos(self):
        return self.tom[0].position()

    def reset(self):
        for i in self.tom:
            i.goto(-700, -700)
        self.tom.clear()
        self.createsnake()





