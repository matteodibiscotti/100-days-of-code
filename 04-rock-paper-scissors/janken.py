import random

def randomgen():
    randomnum = random.randint(0,2)
    return randomnum

def main():
    moves = {0:"rock", 1:"scissors", 2:"paper"}
    print("Let's play ROCK SCISSORS PAPER!!!")
    usermove = int(input("Enter '0' for rock, '1' for scissors or '2' for paper\n"))
    while usermove not in [0, 1, 2]:
        print("You need to select a number between 0 and 2 which reflects your chosen move")
        usermove = input("Enter '0' for rock, '1' for scissors or '2' for paper\n")
    computermove = randomgen()
    if computermove == 0:
        print(f"Computer played {moves[0]}")
    elif computermove == 1:
        print(f"Computer played {moves[1]}")
    else:
        print(f"Computer played {moves[2]}")

    if (usermove == 0 and computermove == 1) or (usermove == 1 and computermove == 2) or (usermove == 2 and computermove == 0):
        print ("You win!!")
    else:
        print("You lose :(")

if __name__ == "__main__":
    main()