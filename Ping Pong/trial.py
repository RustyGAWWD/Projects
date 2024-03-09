from turtle import Turtle, Screen

screen = Screen()
tim = Turtle("square")
tom = Turtle("square")
tim.up()
tim.goto(-292, 0)
tim.shapesize(1, 5)
tom.shapesize(.8, .8)
print(tim.distance(tom))
screen.exitonclick()