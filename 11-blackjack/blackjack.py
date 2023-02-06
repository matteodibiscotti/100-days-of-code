import art, random
from time import sleep

def deal(deck, user_hand):
    random_selection = random.choice(deck)
    user_hand.append(random_selection)
    deck.remove(random_selection)

    return deck, user_hand

def dealer_display_hand(dealer_hand):
    display_hand = []
    for i in dealer_hand:
        display_hand.append(i)
    display_hand[1] = "HIDDEN"

    return display_hand

def score_calc(scores, player_hand, player_name):
    for i in range(len(player_hand)):
        if player_hand[i] in ['J', 'Q', 'K']:
            scores[player_name] += 10
        elif player_hand[i] == 'A' and (scores[player_name] + 11) <= 21:
            scores[player_name] += 11
        elif player_hand[i] == 'A' and (scores[player_name] + 11) > 21:
            scores[player_name] += 1
        else:
            scores[player_name] += player_hand[i]
    
    return scores

def main():
    print(art.logo)
    print("Welcome to BLACKJACK!")
    play = 'y'
    while play != 'n':
        deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,
                'J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
        hand, dealer_hand = [], []
        scores = {'player': 0, 'dealer': 0}
        for i in range(2):                          # Deals the initial hand for each party
            deck, hand = deal(deck, hand)
            deck, dealer_hand = deal(deck, dealer_hand)
        scores = score_calc(scores, hand, 'player')    #calc both player scores
        scores = score_calc(scores, [dealer_hand[0]], 'dealer')   # calc the score of the dealer but only the first card
        display_hand = dealer_display_hand(dealer_hand) #creates the list of the dealers hand with the second card hidden
        
        print(f"Your starting hand is: {hand} and your score is: {scores['player']}")
        print(f"The dealers starting hand is: {display_hand} and their score is: {scores['dealer']}")

        # players draws
        hit = 'h'
        while hit == 'h':
            hit = input('Would you like to hit or stay? Enter "h" to hit or "s" to stay:\n')
            if hit == 's':
                break
            deck, hand = deal(deck, hand)
            scores = {'player': 0, 'dealer': 0}
            scores = score_calc(scores, hand, 'player')
            if scores['player'] <= 21:
                print(f"Your hand is {hand} with a score of {scores['player']}")
                continue
            elif scores['player'] > 21:
                print(f"Your hand is {hand} with a score of {scores['player']}")
                print("You BUST!")
                sleep(1)
                play = input("Would you like to play again? 'y for yes, 'n' for no:\n")
                if play == 'y':
                    main()
                else:
                    play = 'n'
                    break

        # dealer draws
        hit = 'h'
        print ('Dealers turn..')
        sleep(1)
        scores = {'player': 0, 'dealer': 0}
        scores = score_calc(scores, dealer_hand, 'dealer') # Need to do this because score was only calc'd for hidden
        print (f"Dealers hand is {dealer_hand} with a score of {scores['dealer']}")
        while hit == 'h':
            sleep(1)
            deck, dealer_hand = deal(deck, dealer_hand)
            scores = score_calc(scores, dealer_hand, 'dealer')
            if scores['dealer'] <= scores['player']:
                print (f"Dealers hand is {dealer_hand} with a score of {scores['dealer']}")
                continue    
            elif scores['dealer'] == 21 and scores['player'] == 21:
                print("The game is a TIE")
                sleep(1)
                play = input("Would you like to play again? 'y for yes, 'n' for no\n")
                if play == 'y':
                    main()
                else:
                    play = 'n'
            # elif scores['dealer'] < scores['player']:
            #     continue
            else:
                print (f"Dealers hand is {dealer_hand} with a score of {scores['dealer']}")
                sleep(1)
                print('Dealer BUSTS! You WIN')
                sleep(1)
                play = input("Would you like to play again? 'y for yes, 'n' for no\n")
                if play == 'y':
                    main()
                else:
                    play = 'n'
                    break


if __name__ == "__main__":
    main()
