test_word :str = input("Enter a word or text: ").lower()

def is_palindrome(word: str) -> bool:
    """returns True if word is palindrome, Flase otherwise"""
    rev_word = word[::-1] # is palindrome
    if rev_word == word:
        return True
    else:
        return False

def converte(text: str) -> str:
    """returns the converted text as a single word"""
    return ''.join([char for char in text if char.isalnum])


converted_text = converte(test_word)
print(is_palindrome(converted_text))
