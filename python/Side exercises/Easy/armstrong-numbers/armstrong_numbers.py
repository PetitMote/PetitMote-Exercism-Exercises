def is_armstrong_number(number: int) -> bool:
    digits_sum: int = 0
    number_len = len(str(number))
    for i in str(number):
        digits_sum += int(i) ** number_len
    return digits_sum == number
