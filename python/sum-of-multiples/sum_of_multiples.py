def sum_of_multiples(limit, multiples):
    number = 0
    sum = 0
    while number < limit:
        for item in multiples:
            if item == 0:
                continue
            if number % item == 0:
                sum += number
                break
        number += 1
    return sum

