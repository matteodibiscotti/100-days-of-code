def main():
    print("Welcome to TREASURE ISLAND!!!\nYour mission is to find the missing TREASURE!")
    choice = str.lower(input("left or right?\n"))
    while choice not in ["left", "right"]:
        print("You must enter 'left' or 'right'")
        choice = str.lower(input("left or right?\n"))
    if choice == "right":
        print("Game over!")
    choice = str.lower(input("swim or wait?\n"))
    while choice not in ["swim", "wait"]:
        print("You must enter 'swim' or 'wait'")
        choice = str.lower(input("swim or wait?\n"))
    if choice == "swim":
        print("Game over!")
    choice = str.lower(input("Which door? red, yellow or blue?\n"))
    while choice not in ["red", "yellow", "blue"]:
        print('You must enter "red", "yellow" or "blue"')
        choice = str.lower(input("Which door? red, yellow or blue?\n"))
    if choice != "yellow":
        print("Game over!")
    else:
        print("Well done!! You FOUND the TREASURE!!")
    

if __name__ == "__main__":
    main()