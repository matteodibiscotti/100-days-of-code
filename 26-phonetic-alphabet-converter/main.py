import pandas as pd

def main():
    data = pd.read_csv("nato_phonetic_alphabet.csv")
    alphabet = {row["letter"]:row["code"] for (index, row) in data.iterrows()} # Dictionary comprehension

    word = input("Enter the word you want to translate into NATO phonetic:\n").upper()
    # translated_word = []
    # for letter in word:
    #     for (key, value) in alphabet.items():
    #         if key == letter:
    #             translated_word.append(value)
    translated_word = [alphabet[letter] for letter in word] # List comprehension

    print(translated_word)

if __name__ == "__main__":
    main()