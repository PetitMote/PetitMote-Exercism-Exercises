def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    return [candidate for candidate in candidates if check_anagrams(word, candidate)]


def check_anagrams(word1: str, word2: str) -> bool:
    if word1.upper() == word2.upper():
        return False
    elif sorted(word1.upper()) == sorted(word2.upper()):  # It's really frustrating that I didn't find this by myself
        return True
    else:
        return False
