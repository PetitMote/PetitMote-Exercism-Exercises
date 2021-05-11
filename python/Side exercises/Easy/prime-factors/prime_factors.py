def factors(value) -> list[int]:
    """Return the prime factors of the given int."""
    if value <= 1:
        return []
    else:
        prime_factors = []
        first_factor = find_first_factor(value)
        prime_factors.append(first_factor)
        while value // first_factor != 1:
            value = value // first_factor
            first_factor = find_first_factor(value)
            prime_factors.append(first_factor)
        return prime_factors


def find_first_factor(value: int) -> int:
    """Find the first prime factor of the given int."""
    if value % 2 == 0:
        return 2
    else:
        for i in range(3, int(value ** (1/2)) + 1, 2):
            if value % i == 0:
                return i
        return value
