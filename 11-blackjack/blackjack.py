import art, random

# def first_deal(deck, hand, dealer_hand):
#     for i in range(2):
#         random_selection = random.choice(deck)
#         hand.append(random_selection)
#         deck.remove(random_selection)
#         random_selection = random.choice(deck)
#         dealer_hand.append(random_selection)
#         deck.remove(random_selection)

#     return deck, hand, dealer_hand

def deal(deck, user_hand):
    random_selection = random.choice(deck)
    user_hand.append(random_selection)
    deck.remove(random_selection)

def dealer_display_hand(dealer_hand):
    display_hand = dealer_hand
    dealer_hand[1] = "HIDDEN"

    return display_hand

# def score_calc(player, dealer):
#     scores = {'player': 0, 'dealer': 0}
#     players = [player, dealer]
#     player_names = ['player', 'dealer']
#     for i in range(len(players)):
#         for j in players[i]:
#             if j in ['J', 'Q', 'K']:
#                 scores[player_names[i]] += 10
#             elif i == 'A' and (user_score + 11) <= 21:
#                 scores[player_names[i]] += 11
#             elif i == 'A' and (user_score + 11) > 21:
#                 scores[player_names[i]] += 1
#             else:
#                 scores[player_names[i]] += i
    
#     return scores

def score_calc(scores, player_hand, player_name):
    for i in player_hand:
        if i in ['J', 'Q', 'K']:
            scores[player_name[i]] += 10
        elif i == 'A' and (user_score + 11) <= 21:
            scores[player_name[i]] += 11
        elif i == 'A' and (user_score + 11) > 21:
            scores[player_name[i]] += 1
        else:
            scores[player_name[i]] += i
    
    return scores

def main():
    print(art.logo)
    print("Welcome to BLACKJACK!")
    play = 'y'
    while play == 'y':
        deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,
                'J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
        hand, dealer_hand = [], []
        scores = {'player': 0, 'dealer': 0}
        for i in range(2):                          # Deals the initial hand for each party
            deck, hand = deal(deck, hand)
            deck, dealer_hand = deal(deck, dealer_hand)
        scores = score_calc(scores, hand, 'player')    #calc both player scores
        scores = score_calc(scores, dealer_hand[0], 'dealer')   # calc the score of the dealer but only the first card
        #deck, hand, dealer_hand = first_deal(deck, hand, dealer_hand)
        display_hand = dealer_display_hand(dealer_hand) #creates the list of the dealers hand with the second card hidden
        
        print(f"Your starting hand is: {hand} and your score is: {scores['player']}")
        print(f"The dealers starting hand is: {display_hand} and their score is: {scores['dealer']}")

# players draws
        hit = 'h'
        while hit == 'h':
            hit = input('Would you like to hit or stay? Enter "h" to hit or "s" to stay:\n')
            deck, hand = deal(deck, hand)
            scores = score_calc(scores, hand, 'player')
            if scores['player'] <= 21:
                continue
            else:
                print("You BUST!")
                play = input("Would you like to play again? 'y for yes, 'n' for no")
                if play == 'y':
                    main()

# dealer draws
        hit = 'h'
        print ('Dealers turn..')
        while hit == 'h':
            sleep(1)
            while scores['dealer'] <= 21 or scores['dealer'] <= scores['player']:
                deck, dealer_hand = deal(deck, dealer_hand)
                scores = score_calc(scores, dealer_hand, 'dealer')
                if scores['dealer'] == 21 and scores['player'] == 21:
                    print("The game is a TIE")
                    sleep(1)
                    play = input("Would you like to play again? 'y for yes, 'n' for no")
                    if play == 'y':
                        main()
                    else:
                        play = 'n'
                if scores['dealer'] < 21 and scores['dealer'] <= scores['player']:
                    continue
                else:
                    print('You WIN')
                    sleep(1)
                    play = input("Would you like to play again? 'y for yes, 'n' for no")
                    if play == 'y':
                        main()


if __name__ == "__main__":
    main()

# when the cards are dealt both the dealer and the player receive 2 cards but one of the dealers cards is face down
# the player gets to hit as many times as they want until they stay
# then the dealer flips their facedown card and continues to hit until they beat the player score or bust

# option to hit or stay

# check the current total - if ace in hand and score above 21 ace is one otherwise its 11


# Score calc
    # for i in hand:
    #     if i in ['J', 'Q', 'K']:
    #         user_score += 10
    #     elif i == 'A' and (user_score + 11) <= 21:
    #         user_score += 11
    #     elif i == 'A' and (user_score + 11) > 21:
    #         user_score += 1
    #     else:
    #         user_score += i
    # for i in dealer_hand:
    #     if i in ['J', 'Q', 'K']:
    #         dealer_score += 10
    #     elif i == 'A' and (user_score + 11) <= 21:
    #         dealer_score += 11
    #     elif i == 'A' and (user_score + 11) > 21:
    #         dealer_score += 1
    #     else:
    #         dealer_score += i
