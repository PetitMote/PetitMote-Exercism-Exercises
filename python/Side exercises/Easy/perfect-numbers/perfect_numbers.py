# Thanks @Migwel and @ache on Zeste de Savoir for the help on the optimisation ;)
from math import ceil


def classify(number: int) -> str:
    """Classify the int following the Nicomachus' classification of perfect numbers.
    """
    classification: str = ""
    if number < 1 or int(number) != number:
        raise ValueError("Can't classify this number or value")
    elif number == 1:
        classification = "deficient"
    else:
        aliquot = aliquot_sum(number)
        if aliquot > number:
            classification = "abundant"
        elif aliquot < number:
            classification = "deficient"
        else:
            classification = "perfect"
    return classification


def aliquot_sum(number: int) -> int:
    aliquot: int = 1
    sqrt_ceil = ceil(number ** (1/2))
    for i in range(2, ceil(number ** (1 / 2))):
        # Let's say number = X * Y. If we find X, then we find Y. So we can add Y to aliquot.
        if number % i == 0:
            aliquot += i
            aliquot += number / i
    if sqrt_ceil ** 2 == number:
        # If sqrt_ceil ** 2 == number, then the sqrt was an integer, and we excluded it our loop. We need to add it
        # only 1 time now.
        aliquot += number ** (1/2)
    return aliquot
