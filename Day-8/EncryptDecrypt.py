import art 

print("Welcome to Encryption Program")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

#Method One
'''
def encrypt(text , shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The Encoded Text is : {cipher_text}")
    
def decrypt(text , shift):
    cipher_text =""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The Decoded Text is : {cipher_text}") '''

def caesar(direction , text , shift):
    empty_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            empty_text += alphabet[new_position]
        else:
            empty+=char
    print(f"The {direction} text is : {empty_text}")

Go_Again = True
while Go_Again:
    direction = input("Type 'Encode' for Encrypt and 'Decode' for Decrypt : ").lower()
    text = input("Enter your Text : ")
    shift = int(input("Enter the Shift Number : "))
    shift %= 26
    caesar(direction , text , shift)
    
    result = input("Do you wanna go again? Yes or No : ").lower()
    if result == "no":
        Go_Again = False
        print("GoodBye ! 👋👋")