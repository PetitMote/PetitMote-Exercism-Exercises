# Learned about the zip function and that I should call maths functions on booleans

def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Strings are not the same length")
    # Found on the internet - I guess it's more Pythonic than the intuitive answer I found (before finding this)
    # Though, I don't like depending on the internal mechanic that translates True to 1
    nb_errors = sum([a != b for a, b in zip(strand_a, strand_b)])
    return nb_errors
