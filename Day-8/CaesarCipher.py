import art

print("Welcome to Encryption Program")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(art.logo)

'''def encrypt(text , shift):
    cipter_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipter_text += new_letter
    print(f"The Encoded Text is : {cipter_text}")
    
def decrypt(text , shift):
    decrypted_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        decrypted_text += new_letter
    print(f"The Decryped Text is {decrypted_text}")
    
if direction == "encode":
    encrypt(text , shift)
elif direction == "decode":
    decrypt(text , shift)
    '''


def caesar(direction, text, shift):
    cipher_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"The {direction} text is : {cipher_text}")

        
continue_Loop = True
while continue_Loop:
    direction = input("Type 'encode' to Encrypt , type 'decode' to Decrypt :\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the Shift Number:\n"))
    shift = shift % 26
    caesar(direction , text , shift)  
        
    result = input("Do you wanna go again? yes or no : ").lower()
    if result == "no":
        continue_Loop = False
        print("Goodbye 👋")