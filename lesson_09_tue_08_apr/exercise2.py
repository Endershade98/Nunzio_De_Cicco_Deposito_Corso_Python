text = input("Enter your text: ")

# check the duplicates
def is_duplicate(word):
    if word in text.split():
        count = 0
        for word in text:
            count += 1
        if count >= 2: # verifies if word has a duplicate
            print(word, "has length", len(word))
            print(word, "has", count,"duplicate")

# split the text as a list of words
def converte(text):
    """returns the converted text as a single word"""
    return ''.join([char for char in text if char.isalpha])

print(is_duplicate(text))

# count the number of words in text
def count(text):
    word_dict = {w: (is_duplicate(text).count(w), len(w)) for w in is_duplicate(text)}
    for k, (v1, v2) in word_dict.items():
        if v1 > 1:
            print(f"{k} has {v1} occurrences and", v2, "is the number of character")

