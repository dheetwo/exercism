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

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    if len(list_one) == len(list_two):
        for index, item in enumerate(list_one):
            if not(item == list_two[index]):
                return UNEQUAL
        return EQUAL
    elif len(list_one) < len(list_two):
        list_two_spliced = []
        for index, item in enumerate(list_two):
            list_two_spliced.append(list_two[index:index + len(list_one)])
        if list_one in list_two_spliced:
            return SUBLIST
    elif len(list_two) < len(list_one):
        list_one_spliced = []
        for index, item in enumerate(list_one):
            list_one_spliced.append(list_one[index:index + len(list_two)])
        if list_two in list_one_spliced:
            return SUPERLIST
    return UNEQUAL
