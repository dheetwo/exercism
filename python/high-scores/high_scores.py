def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_three = []
    for i in range(0, 3):
        if len(scores) > 0:
            top_three.append(scores.pop(scores.index(max(scores))))
    return top_three
