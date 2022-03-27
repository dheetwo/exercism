def steps(number):
    counter = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number > 1:
        if number % 2 == 0:
            number = int(number/2)
        elif number % 2 == 1:
            number *= 3
            number += 1
        counter += 1
    return counter
