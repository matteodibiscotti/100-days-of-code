import turtle as t
import random

matt = t.Turtle()
t.colormode(255)

matt.pensize(10)
matt.speed('fastest')
angles = [0, 90, 180, 270]

def random_colour_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)

    return colour

while True:
    matt.color(random_colour_gen())
    matt.setheading(random.choice(angles))
    matt.forward(30)