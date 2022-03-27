def is_triangle(sides):
    """
    :param sides:
    :return:
    """
    return sides[0] > 0 and sides[1] > 0 and 0 < sides[2] < sides[0] + sides[1] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]

def equilateral(sides):
    """
    :param sides:
    :return:
    """
    return sides[0] == sides[1] == sides[2] and is_triangle(sides)

def isosceles(sides):
    """
    :param sides:
    :return:
    """
    return (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]) and is_triangle(sides)


def scalene(sides):
    """
    :param sides:
    :return:
    """
    return not equilateral(sides) and not isosceles(sides) and is_triangle(sides)
