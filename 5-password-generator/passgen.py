import random, string

letters = string.ascii_letters
numbers = string.digits
punc = string.punctuation

def main():
    print("Welcome to the Python Password Generator")
    passwd_letters = int(input("How many letters would you like in your password?\n")) # code 0 for selection
    passwd_numbers = int(input("How many numbers would you like in your password?\n")) # code 1 for selection
    passwd_punc = int(input("How many special characters would you like in your password?\n")) # code 2 for selection
    total_len = passwd_letters + passwd_numbers + passwd_punc
    total_len_count, letters_count, number_count, punc_count = 0, 0, 0, 0
    password = ""
    selector = [0, 1, 2]
    while total_len_count < total_len:
        char_type = random.choice(selector)
        if char_type == 0 and letters_count < passwd_letters:
            password += (random.choice(letters))
            letters_count += 1
            total_len_count += 1
            if letters_count == passwd_letters:
                selector.remove(0)
        elif char_type == 1 and number_count < passwd_numbers:
            password += (random.choice(numbers))
            number_count += 1
            total_len_count += 1
            if number_count == passwd_numbers:
                selector.remove(1)
        elif char_type == 2 and punc_count < passwd_punc:
            password += (random.choice(punc))
            punc_count += 1
            total_len_count += 1
            if punc_count == passwd_punc:
                selector.remove(2)
    
    print("Here is your password:\n" + password)

if __name__ == "__main__":
    main()