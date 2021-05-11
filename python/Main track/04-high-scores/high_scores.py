# Thank you @IsaacG for the review

def latest(scores: list[int]) -> int:
    """
    Return the latest score (last element in the list).
    """
    return scores[-1]


def personal_best(scores: list[int]) -> int:
    """
    Return the best score (highest element in the list).
    """
    return max(scores)


def personal_top_three(scores: list[int]) -> list[int]:
    """
    Return the three or less highest scores (highest elements in the list).
    """
    return sorted(scores, reverse=True)[:3]
