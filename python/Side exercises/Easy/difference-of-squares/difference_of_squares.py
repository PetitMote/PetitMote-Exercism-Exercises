def square_of_sum(number: int) -> int:
    return (number * (number + 1) / 2) ** 2


def sum_of_squares(number: int) -> int:
    return number * (2 * number + 1) * (number + 1) / 6


def difference_of_squares(number: int) -> int:
    return square_of_sum(number) - sum_of_squares(number)
