def is_palindrome(number):
    temp = number
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10
    return number == reverse


def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    factors_tuple = tuple(range(max_factor, min_factor - 1, -1))
    factors_tuple2 = tuple(range(max_factor, min_factor - 1, -1))
    largest_palindrome = 0
    factors_list = []
    for item1 in factors_tuple:
        for item2 in factors_tuple2:
            if largest_palindrome > 0 and (item1 * item2 < largest_palindrome):
                continue
            if is_palindrome(item1 * item2):
                if item1 * item2 > largest_palindrome:
                    factors_list.clear()
                    largest_palindrome = item1 * item2
                    if item1 <= item2:
                        factors_list.append((item1, item2))
                    else:
                        factors_list.append((item2, item1))
                elif item1 * item2 == largest_palindrome:
                    if item1 <= item2:
                        factors_list.append((item1, item2))
                    else:
                        factors_list.append((item2, item1))
    if largest_palindrome == 0:
        largest_palindrome = None
    return largest_palindrome, list(set(factors_list))


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    factors_tuple = tuple(range(min_factor, max_factor + 1))
    factors_tuple2 = tuple(range(min_factor, max_factor + 1))
    smallest_palindrome = 0
    factors_list = []
    for item1 in factors_tuple:
        for item2 in factors_tuple2:
            if smallest_palindrome > 0 and (item1 * item2 > smallest_palindrome):
                continue
            if is_palindrome(item1 * item2) and item1 * item2 > 0:
                if smallest_palindrome == 0:
                    smallest_palindrome = item1 * item2
                    if item1 <= item2:
                        factors_list.append((item1, item2))
                    else:
                        factors_list.append((item2, item1))
                elif item1 * item2 < smallest_palindrome:
                    factors_list.clear()
                    smallest_palindrome = item1 * item2
                    if item1 <= item2:
                        factors_list.append((item1, item2))
                    else:
                        factors_list.append((item2, item1))
                elif item1 * item2 == smallest_palindrome:
                    if item1 <= item2:
                        factors_list.append((item1, item2))
                    else:
                        factors_list.append((item2, item1))
    if smallest_palindrome == 0:
        smallest_palindrome = None
    return smallest_palindrome, list(set(factors_list))