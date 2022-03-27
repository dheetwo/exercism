def marker_at_top_left_corner(position, left, top):
    return position == (left, top)

def marker_at_top_right_corner(position, right, top):
    return position == (right, top)

def marker_at_bottom_right_corner(position, right, bottom):
    return position == (right, bottom)

def marker_at_bottom_left_corner(position, left, bottom):
    return position == (left, bottom)


def row_complete(matrix, row):
    for item in matrix[row]:
        if item is None:
            return False
    return True


def column_complete(matrix, column):
    for item in matrix:
        if item[column] is None:
            return False
    return True


def spiral_matrix(size):
    x_pos = 0
    y_pos = 0
    x_direction = 0
    y_direction = 0
    matrix = [[None] * size for _ in range(size)]
    left_border = 0
    right_border = size - 1
    top_border = 0
    bottom_border = size - 1
    for number in range(1, pow(size, 2) + 1):
        marker = (x_pos, y_pos)
        if marker_at_top_left_corner(marker, left_border, top_border):
            x_direction = 1
            y_direction = 0
        if marker_at_top_right_corner(marker, right_border, top_border):
            x_direction = 0
            y_direction = 1
        if marker_at_bottom_right_corner(marker, right_border, bottom_border):
            x_direction = -1
            y_direction = 0
        if marker_at_bottom_left_corner(marker, left_border, bottom_border):
            x_direction = 0
            y_direction = -1
        if row_complete(matrix, top_border):
            top_border += 1
        if row_complete(matrix, bottom_border):
            bottom_border -= 1
        if column_complete(matrix, right_border):
            right_border -= 1
        if column_complete(matrix, left_border):
            left_border += 1
        matrix[y_pos][x_pos] = number
        x_pos += x_direction
        y_pos += y_direction
    return matrix