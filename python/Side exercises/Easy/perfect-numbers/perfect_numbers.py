# TO-DO : optimise the function, takes currently 4 seconds to run the tests

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
    for i in range(2, int(number ** (1 / 2))+1):
        # Let's say number = X * Y. If we find X, then we find Y. So we can add Y to aliquot.
        if number % i == 0:
            aliquot += i
            aliquot += number / i
    if int(number ** (1/2)) == number ** (1/2):
        # If sqrt(number) is an integer, then we added it 2 times. Here, we correct that by subtracting it if necessary.
        aliquot -= number ** (1/2)
    return aliquot
