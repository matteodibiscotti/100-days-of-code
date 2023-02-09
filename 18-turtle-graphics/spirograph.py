import turtle as t
import random

matt = t.Turtle()
t.colormode(255)
matt.speed('fastest')

def random_colour_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)

    return colour

while True:
    matt.circle(150, 360)
    matt.right(2)
    matt.color(random_colour_gen())