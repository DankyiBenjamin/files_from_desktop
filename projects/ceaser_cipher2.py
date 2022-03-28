import string

encryped_text = input("please type in the test you want to decrypt using ceaser cipher: ")

SHIFT = (26-3)

def decryption():
    alphabet = string.ascii_uppercase
    shifted = alphabet[SHIFT:] + alphabet[:SHIFT]
    table = str.maketrans(alphabet, shifted)


    decrypted = encryped_text.translate(table)
    print(decrypted)


decryption()