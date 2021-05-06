def is_armstrong_number(number: int) -> bool:
    number_len = len(str(number))
    digits_sum = sum(int(i) ** number_len for i in str(number))
    return digits_sum == number
