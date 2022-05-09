def triplets_with_sum(number):
    triplets = []
    for a in range(1, number):
        denom = 2 * (number - a)
        num = 2 * a ** 2 + number ** 2 - 2 * number * a
        if denom > 0 and num % denom == 0:
            c = num // denom
            b = number - a - c
            if b > a:
                triplets.append((a, b, c))
    return triplets


print(triplets_with_sum(30000))
