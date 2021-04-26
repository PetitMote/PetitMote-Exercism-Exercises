"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Score categories.
# Change the values as you see fit.

YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice: list, category):
    if category < 7:
        points = ones_to_sixes(dice, category)
        return points
    else:
        list_functions = [full_house, four_of_a_kind, little_straight, big_straight, choice, yacht]
        dice.sort()
        points = list_functions[category - 7](dice)
        return points


def ones_to_sixes(dice: list, category):
    n = dice.count(category)
    return dice.count(category) * category


def full_house(dice: list):
    n = [dice.count(dice[0]), dice.count(dice[4])]
    n.sort()

    if n == [2, 3]:
        return sum(dice)
    else:
        return 0


def four_of_a_kind(dice: list):
    if dice.count(dice[0]) >= 4:
        return dice[0] * 4
    elif dice.count(dice[4]) == 4:
        return dice[4] * 4
    else:
        return 0


def little_straight(dice: list):
    if dice == [1, 2, 3, 4, 5]:
        return 30
    else:
        return 0


def big_straight(dice: list):
    if dice == [2, 3, 4, 5, 6]:
        return 30
    else:
        return 0


def choice(dice: list):
    return sum(dice)


def yacht(dice: list):
    if dice[0] == dice[4]:
        return 50
    else:
        return 0


print(score([2, 2, 2, 1, 1], 7))
