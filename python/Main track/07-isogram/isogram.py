import re
import string


def is_isogram(word: str) -> bool:
    """Return true if the word is an isogram (only 1 occurence of each letter used"""
    word = word.upper()  # So we don't have to manage lower and upper case
    word = "".join(re.findall("[A-Z]", word))  # Remove everything else than uppercase letters
    alphabet = list(string.ascii_uppercase)

    for letter in word:
        if letter in alphabet:
            alphabet.remove(letter)
        else:
            return False

    return True
