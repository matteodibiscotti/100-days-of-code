import turtle as t
import random

t.colormode(255)

matt = t.Turtle()
matt.color("green")
matt.shape("turtle")
matt.penup()

yuu = t.Turtle()
yuu.color((222,165,164))
yuu.shape("turtle")
yuu.penup()

tetoh = t.Turtle()
tetoh.color("brown")
tetoh.shape("turtle")
tetoh.penup()

sunchan = t.Turtle()
sunchan.color("yellow")
sunchan.shape("turtle")
sunchan.penup()

contestants = {matt:'green', yuu:'pink', tetoh:'brown', sunchan:'yellow'}

def main():
    screen = t.Screen()
    screen.setup(width=500, height=400)

    matt.setpos(-235, 45)
    yuu.setpos(-235, 15)
    tetoh.setpos(-235, -15)
    sunchan.setpos(-235, -45)

    user_bet = screen.textinput(title='Enter your bet', prompt='Which turtle will win the race? Select your colour\nGreen, Pink, Brown, Yellow').lower()
   
    if user_bet:
        is_race_on = True

    while is_race_on:
        for i in contestants:
            i.forward(random.randint(0,10))
            if i.xcor() >= 250:
                is_race_on = False
                winner = contestants[i]
    
    print(f"The winner is {winner}")

    screen.exitonclick()


if __name__ == "__main__":
    main()
