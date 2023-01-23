def main():
    print('Welcome to TIP CALCULATOR!!!')
    total = float(input('What was the total bill amount?\n'))
    tip = float(input('How much (in percent) would you like to tip?\n'))/100
    people = int(input('How many people will be splitting the bill?\n'))
    if tip > 0:
        tip_amount = (total + (total * tip))/people
    else:
        tip_amount = total/people
    print('Each person should pay $' + '{:.2f}'.format(tip_amount))

if __name__ == "__main__":
    main()