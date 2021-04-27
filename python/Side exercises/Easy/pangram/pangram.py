# Need to work on the set object from the community solutions

def is_pangram(sentence):
    alphabet = (
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z")
    sentence = str(sentence).lower()

    for letter in alphabet:
        if letter not in sentence:
            return False

    return True
