# Thanks to @bobahop for the review and the set tip
# Thanks to @adrianmcli for the filter() based solution :
# https://exercism.io/tracks/python/exercises/isogram/solutions/f1b6f252568d41be94b063db3d1a234e

import re
# import string


def is_isogram(word: str) -> bool:
    """Return true if the word is an isogram (only 1 occurence of each letter used."""
    word = word.casefold()  # So we don't have to manage lower and upper case
    word = "".join(re.findall("[a-z]", word))  # Remove everything else than uppercase letters
    # Alternative found on the community solutions :
    # word = filter(str.isalpha(), word)
    if len(word) == len(set(word)):
        return True
    else:
        return False

    # Old solution
    # alphabet = set(string.ascii_lowercase)
    #
    # for letter in word:
    #     if letter in alphabet:
    #         alphabet.remove(letter)
    #     else:
    #         return False
    #
    # return True
