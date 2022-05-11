def primes(limit):
    sequence = list(range(2, limit + 1))
    p = 2
    composite = set()
    while p < limit:
        for number in range(2, limit + 1):
            if number % p == 0 and number != p:
                composite.add(number)
        p += 1
    return sorted(list(set(sequence) - composite))

