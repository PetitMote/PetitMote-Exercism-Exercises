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
    aliquot: int = 0
    for i in range(1, number):
        if number % i == 0:
            aliquot += i
    return aliquot
