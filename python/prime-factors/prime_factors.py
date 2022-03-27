def factors(value):
    factors_list = []
    factor = 2
    while value >= 2:
        print(str(value) + " % " + str(factor))
        if value == 2:
            factors_list.append(value)
            return factors_list
        elif value % factor > 0:
            factor += 1
        else:
            factors_list.append(factor)
            value = int(value/factor)
            factor = 2
    return factors_list