# Score categories.
# Change the values as you see fit.
YACHT = "Yacht"
ONES = "Ones"
TWOS = "Twos"
THREES = "Threes"
FOURS = "Fours"
FIVES = "Fives"
SIXES = "Sixes"
FULL_HOUSE = "Full House"
FOUR_OF_A_KIND = "Quads"
LITTLE_STRAIGHT = "Little Straight"
BIG_STRAIGHT = "Big Straight"
CHOICE = "Choice"


def score(dice, category):
    if category is YACHT:
        if len(set(dice)) == 1:
            return 50
        else:
            return 0
    if category is ONES:
        return dice.count(1)
    if category is TWOS:
        return 2 * dice.count(2)
    if category is THREES:
        return 3 * dice.count(3)
    if category is FOURS:
        return 4 * dice.count(4)
    if category is FIVES:
        return 5 * dice.count(5)
    if category is SIXES:
        return 6 * dice.count(6)
    if category is FULL_HOUSE:
        if len(set(dice)) == 2 and 2 <= dice.count(dice[0]) <= 3:
            return sum(dice)
        else:
            return 0
    if category is FOUR_OF_A_KIND:
        if len(set(dice)) == 1:
            return 4 * dice[0]
        elif len(set(dice)) == 2 and dice.count(dice[0]) == 1:
            return 4 * dice[1]
        elif len(set(dice)) == 2 and dice.count(dice[0]) == 4:
            return 4 * dice[0]
        else:
            return 0
    if category is LITTLE_STRAIGHT:
        if len(set(dice)) == 5 and 6 not in dice:
            return 30
        else:
            return 0
    if category is BIG_STRAIGHT:
        if len(set(dice)) == 5 and 1 not in dice:
            return 30
        else:
            return 0
    if category is CHOICE:
        return sum(dice)
    return 0
