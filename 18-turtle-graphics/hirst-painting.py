import colorgram, random
import turtle as t

colours = colorgram.extract('painting.jpg', 15)
matt = t.Turtle()
t.colormode(255)


def select_colour(colours):
    colour = random.choice(colours)
    rgb = colour.rgb

    return rgb

matt.penup()
matt.setheading(225)
matt.forward(320)
matt.setheading(0)

for j in range(10):
    for _ in range(10):
        matt.dot(20, select_colour(colours))
        matt.forward(50)
    matt.left(90)
    matt.forward(50)
    matt.left(90)
    matt.forward(500)
    matt.setheading(0)

screen = t.Screen()
screen.exitonclick()