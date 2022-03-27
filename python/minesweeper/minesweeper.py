def annotate(minefield):
    # Function body starts here
    if len(minefield) == 0:
        return []
    solution_list = [[0] * len(row) for row in minefield]
    for row_number, row in enumerate(minefield):
        for char in row:
            if not(char == "*" or char == " "):  # invalid input checks
                raise ValueError("The board is invalid with current input.")
        if len(row) != len(minefield[0]):   # unbalanced grid check
            raise ValueError("The board is invalid with current input.")
        for column_number, char in enumerate(minefield[row_number]):
            if 0 < column_number:  # column on the left exists
                if 0 < row_number and minefield[row_number - 1][column_number - 1] == "*":
                    solution_list[row_number][column_number] += 1  # check top left square
                if minefield[row_number][column_number - 1] == "*":
                    solution_list[row_number][column_number] += 1  # check direct left square
                if row_number < len(minefield) - 1 and minefield[row_number + 1][column_number - 1] == "*":
                    solution_list[row_number][column_number] += 1  # check bottom left square
            if column_number < len(minefield[row_number]) - 1:  # column on the right exists
                if 0 < row_number and minefield[row_number - 1][column_number + 1] == "*":
                    solution_list[row_number][column_number] += 1  # check top right square
                if minefield[row_number][column_number + 1] == "*":
                    solution_list[row_number][column_number] += 1  # check direct right square
                if row_number < len(minefield) - 1 and minefield[row_number + 1][column_number + 1] == "*":
                    solution_list[row_number][column_number] += 1  # check bottom right square
            if 0 < row_number and minefield[row_number - 1][column_number] == "*":  # check above
                solution_list[row_number][column_number] += 1
            if row_number < len(minefield) - 1 and minefield[row_number + 1][column_number] == "*":  # check below
                solution_list[row_number][column_number] += 1
    for row_number, row in enumerate(minefield):
        for column_number, char in enumerate(minefield[row_number]):
            if char == "*":
                solution_list[row_number][column_number] = "*"
            if solution_list[row_number][column_number] == 0:
                solution_list[row_number][column_number] = " "
            else:
                solution_list[row_number][column_number] = str(solution_list[row_number][column_number])
    solution = []
    for item in solution_list:
        solution.append("".join(item))
    return solution


