import ascii_art, wordlist, random, string

def main():
    print("\nLet's play...")
    print(ascii_art.logo)
    print("\nRULES\nYou start with 6 lives, every incorrect guess reduces that by 1\nFigure out the word within the number of lives\n")
    word = random.choice(wordlist.word_list)
    #print(word)
    solution = []
    for i in range(len(word)):
        solution.append("_")

    lives = 6
    print(ascii_art.stages[0])
    while lives > 0 and "_" in solution:
        print(solution)
        choice = str.lower(input("Choose a letter:\n"))
        if choice in string.ascii_lowercase:
            if choice in word:
                if choice in solution:
                    print("\nYou already selected this letter, try another\n")
                else:
                    for i in range(len(word)):
                        if word[i-1] == choice:
                            solution[i-1] = choice
            else:
                lives -= 1
                print(ascii_art.stages[6-lives])
                print(f"You have {lives} lives remaining")
        else:
            print("You can only enter alphabetic characters\n")
    if lives == 0:
        print(f"\nThe solution was {word}\n")
        print("You lose, try again\n")
    else:
        print("You WIN!!!")

if __name__ == "__main__":
    main()