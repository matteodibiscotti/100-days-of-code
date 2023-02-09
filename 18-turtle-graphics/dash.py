from turtle import Turtle, Screen

matt = Turtle()
screen = Screen()

for i in range(10):
    matt.forward(10)
    matt.pu()
    matt.forward(10)
    matt.pd()

screen.exitonclick()