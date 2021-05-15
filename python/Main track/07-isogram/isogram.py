# Thanks to @bobahop for the casefold method (better handling of special letters) and for remembering me of using a
# set instead of a list (minor performance improvement)

import re
import string


def is_isogram(word: str) -> bool:
    """Return true if the word is an isogram (only 1 occurence of each letter used."""
    word = word.casefold()  # So we don't have to manage lower and upper case
    word = "".join(re.findall("[a-z]", word))  # Remove everything else than uppercase letters
    alphabet = set(string.ascii_lowercase)

    for letter in word:
        if letter in alphabet:
            alphabet.remove(letter)
        else:
            return False

    return True
