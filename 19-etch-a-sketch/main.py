import turtle as t

matt = t.Turtle()
screen = t.Screen()

def matt_forward():
    matt.forward(10)

def matt_back():
    matt.back(10)

def matt_left():
    new_heading = matt.heading() + 10
    matt.setheading(new_heading)

def matt_right():
    new_heading = matt.heading() - 10
    matt.setheading(new_heading)

def clear_screen():
    matt.clear()
    matt.penup()
    matt.home()
    matt.pendown()

def main():
    screen.listen()
    screen.onkey(key="w", fun=matt_forward)
    screen.onkey(key="s", fun=matt_back)
    screen.onkey(key="a", fun=matt_left)
    screen.onkey(key="d", fun=matt_right)
    screen.onkey(key="c", fun=matt_forward)
    screen.onkey(key="space", fun=clear_screen)
    screen.exitonclick()

if __name__ == "__main__":
    main()