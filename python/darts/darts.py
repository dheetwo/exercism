def score(x, y):
    if pow(x, 2) + pow(y, 2) <= 1:
        return 10
    elif pow(x, 2) + pow(y, 2) <= 25:
        return 5
    elif pow(x, 2) + pow(y, 2) <= 100:
        return 1
    else:
        return 0
