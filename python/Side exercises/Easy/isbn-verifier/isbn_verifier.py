# ## People on exercism use Regular Expressions. I don't like it. But I found this very readable solution :
# https://exercism.io/tracks/python/exercises/isbn-verifier/solutions/aa85f7147f9a468e840f72b31f700fab

def is_valid(isbn: str) -> bool:
    """Check if an ISBN is valid
    """
    isbn = isbn.replace("-", "")
    return check_isbn_formula(isbn) if check_isbn_format(isbn) else False


def check_isbn_format(isbn: str) -> bool:
    """Check that the ISBN uses only numerics or X, and is 10 digits long.
    """
    if len(isbn) != 10:
        return False
    key = isbn[-1]
    isbn = isbn[:-1]
    return isbn.isnumeric() and (key.isnumeric() or key == "X")


def check_isbn_formula(isbn: str) -> bool:
    """Check the result of the formula of an ISBN
    """
    key = isbn[-1]
    isbn = isbn[:-1]
    check: int = 0
    i = 10
    for n in isbn:
        check += i * int(n)
        i -= 1
    if key == "X":
        check += 10
    else:
        check += int(key)
    check = check % 11
    return not check
