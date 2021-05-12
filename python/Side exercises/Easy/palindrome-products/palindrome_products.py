# TODO Absolutely not optimized, I need to check on this solution (when I understand it...) :
#  https://exercism.io/tracks/python/exercises/palindrome-products/solutions/d68cab86cad94d4d821f26da44bb0722

def largest(min_factor, max_factor) -> (int, list[list[int]]):
    if max_factor < min_factor:
        raise ValueError("Invalid arguments : min_actor > max_factor")
    factors = tuple(reversed(range(min_factor, max_factor + 1)))
    palindroms, palindrom_products = find_palindroms(factors)
    if not palindroms:
        return None, []
    else:
        max_value = max(palindroms)
        largest_palindroms = [palindrom_products[i] for i in [j for j, x in enumerate(palindroms) if x == max_value]]
        return max_value, largest_palindroms


def smallest(min_factor, max_factor) -> (int, list[list[int]]):
    if max_factor < min_factor:
        raise ValueError("Invalid arguments : min_actor > max_factor")
    factors = tuple(range(min_factor, max_factor + 1))
    palindroms, palindrom_products = find_palindroms(factors)
    if not palindroms:
        return None, []
    else:
        min_value = min(palindroms)
        smallest_palindroms = [palindrom_products[i] for i in [j for j, x in enumerate(palindroms) if x == min_value]]
        return min_value, smallest_palindroms


def is_palindrom(number) -> bool:
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False


def find_palindroms(factors: list[int]) -> (list[int], list[list[int]]):
    palindrom_products: list[list[int]] = []
    palindroms: list[int] = []
    for i, a in enumerate(factors):
        for b in factors[i:]:
            product = a * b
            if is_palindrom(product):
                palindrom_products.append([a, b])
                palindroms.append(product)
    return palindroms, palindrom_products
