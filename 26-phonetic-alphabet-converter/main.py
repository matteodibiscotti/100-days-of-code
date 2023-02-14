import pandas as pd

def main():
    data = pd.read_csv("nato_phonetic_alphabet.csv")
    alphabet = {row["letter"]:row["code"] for (index, row) in data.iterrows()} # Dictionary comprehension

    def translate():
        word = input("Enter the word you want to translate into NATO phonetic:\n").upper()
        try:
            translated_word = [alphabet[letter] for letter in word] # List comprehension
        except KeyError:
            print("That is not a valid entry containing only letters of the alphabet")
            translated_word = translate()
        else:
            print(translated_word)
    
    translate()

if __name__ == "__main__":
    main()