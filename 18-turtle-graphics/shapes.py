from turtle import Turtle, Screen

matt = Turtle()
screen = Screen()

for i in range(3,11):
    angle = 360/i
    for _ in range(i):
        matt.forward(80)
        matt.right(angle)

screen.exitonclick()