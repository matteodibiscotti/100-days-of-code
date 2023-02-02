import ascii_art, string

alphabet = string.ascii_lowercase

def encrypt(string, shift):
    encrypted_string = ""
    for i in string:
        index = alphabet.find(i)
        encrypted_char = alphabet[(index + shift) % 26]
        encrypted_string += encrypted_char
    return encrypted_string

def decrypt(string, shift):
    decrypted_string = ""
    for i in string:
        index = alphabet.find(i)
        decrypted_char = alphabet[(index - shift) % 26]
        decrypted_string += decrypted_char
    return decrypted_string

def main():
    print(ascii_art.logo)
    print("Welcome to the Caesar Cipher encrypter/decrypter")
    action = int(input("Would you like to encrypt or decrypt your string? (select '1' for encrypt or '2' for decrypt\n"))
    if action == 1:
        string = input("Please enter the string you would like to encrypt:\n").lower()
        shift = int(input("Enter the shift/key\n"))
        print(encrypt(string, shift))
    else:
        string = input("Please enter the string you would like to decrypt:\n").lower()
        shift = int(input("Enter the shift/key\n"))
        print(decrypt(string, shift))
    
if __name__ == "__main__":
    main()