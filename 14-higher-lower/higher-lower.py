import game_data, art, random
from time import sleep

def select_challengers(challenger):
    challenger1 = random.choice(challenger)
    remaining_choices = [i for i in challenger if i != challenger1]
    challenger2 = random.choice(remaining_choices)

    return challenger1, challenger2

def display_question(challenger1, challenger2):
    print(f"Compare A: {challenger1['name']}, a {challenger1['description']} from {challenger1['country']}\n")
    print(art.vs + "\n")
    print(f"Against B: {challenger2['name']}, a {challenger2['description']} from {challenger2['country']}\n")
    user_answer = input("Who has more followers? Select 'A' or 'B'\n").lower()

    return user_answer

def check_answer(challenger1, challenger2, user_answer, score):
    follower_counts = [challenger1['follower_count'], challenger2['follower_count']]
    correct_answer = follower_counts.index(max(follower_counts))
    if (user_answer == 'a' and correct_answer == 0) or (user_answer == 'b' and correct_answer == 1):
        score += 1
        print(f"You are correct! Your current score is {score}\n\n")
        correct = True
        sleep(1)
    else:
        print(f"Sorry that is the wrong answer\nYou ended with a score of {score}")
        sleep(1)
        correct = False

    return score, correct

def main():
    print(art.logo + "\n")
    print("Welcome to HIGHER or LOWER\n")
    score = 0
    playing = True
    while playing == True:
        challenger1, challenger2 = select_challengers(game_data.data)
        user_answer = display_question(challenger1, challenger2)
        score, correct = check_answer(challenger1, challenger2, user_answer, score)
        if correct == False:
            playing = False

if __name__ == "__main__":
    main()
