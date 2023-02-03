# SUGGESTED IMPROVEMENTS
#  - input validation
#  - check bids are of type float or int
#  - check names do not include numbers
#  - get the numbers to always have 2 decimal places

def main():
    print("Welcome to the silent auction")
    more_bidders = True
    bids = {}
    highest_bid = 0
    while more_bidders == True:
        name = input("Enter your name: ")
        bid = float(format(float(input("Enter your maximum bid: ")), '.2f'))
        bids[name] = bid
        add_bidder = ""
        while add_bidder != "yes" and add_bidder != "no":
            add_bidder = input("Are there any other bidders?\nEnter 'yes' or 'no'\n").lower()
        if add_bidder == "no":
            more_bidders = False
    for i in bids:
        if bids[i] > highest_bid:
            highest_bid = bids[i]
            winner = i  
    print (f'The winner is {winner} with a bid of ${highest_bid}')

if __name__ == "__main__":
    main()