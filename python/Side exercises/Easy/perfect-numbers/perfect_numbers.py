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
        aliquot_sum = sum(find_factors(number))
        if aliquot_sum > number:
            classification = "abundant"
        elif aliquot_sum < number:
            classification = "deficient"
        else:
            classification = "perfect"
    return classification


def find_factors(number: int) -> list[int]:
    factors: list[int] = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    return factors
