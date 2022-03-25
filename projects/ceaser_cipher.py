import string
# text to encrypt are typed here 
plain_text = input("please type the word you want to encrypt: ").upper()
print(plain_text)

shift = 3%26

def encryption():
    alphabet = string.ascii_uppercase
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)

    encrypted = plain_text.translate(table)
    print(encrypted)

encryption()