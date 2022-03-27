def square(number):
    if number <= 0 or number > 64:
        raise ValueError('square must be between 1 and 64')
    return pow(2, number-1)


def total():
    value_at_square = []
    for i in range(64):
        value_at_square.append(square(i+1))
    return sum(value_at_square)

