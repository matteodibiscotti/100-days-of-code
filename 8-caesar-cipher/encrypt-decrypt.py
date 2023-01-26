import ascii_art

def encrypt(string, shift):
    # stuff

def decrypt(string, shift):
    # stuff

def main():
    print(ascii_art.logo)
    print("Welcome to the Caesar Cipher encrypter/decrypter")
    action = int(input("Would you like to encrypt or decrypt your string? (select '1' for encrypt or '2' for decrypt\n\n"))
    if action == 1:
        string = input("Please enter the string you would like to encrypt:\n\n")
        shift = input("Enter the shift/key")
        encrypt(string, shift)
    else:
        string = input("Please enter the string you would like to decrypt:\n\n")
        shift = input("Enter the shift/key")
        decrypt(string, shift)
    
if __name__ == "__main__":
    main()


'''
show the ascii art
greeting to the tool
ask for the string to encrypt
ask for the number of shifts
loop through the string
match the letter in the string to the letter in the alphabet and return its position
add the number of shifts to the position of the matched letter and return the letter at that position
append that letter to an empty string
print the output

for decoding just do the opposite

make an encode function and a decode function
ask the user to choose

'''