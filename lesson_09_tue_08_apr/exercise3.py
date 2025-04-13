alphabet = "abcdefghijklmnopqrstuvz"

def caesar_cipher(word: str, shift: int) -> str:
    result = ""
    for char in word:
        if char.isalpha():
            for i in alphabet:
                position[i] += shift
            
            
#def decode(word, -shift):
    pass

def menu():
    pass