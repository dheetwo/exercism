class Matrix:
    matrix_list = []

    def __init__(self, matrix_string):
        self.matrix_list = matrix_string.split("\n")


    def row(self, index):
        rows = []
        for row in self.matrix_list:
            rows.append(row.split(' '))
        for row_number, row in enumerate(rows):
            for column_number, number in enumerate(row):
                try:
                    rows[row_number][column_number] = int(number)
                except ValueError:
                    print("Invalid matrix string input")
        return rows[index - 1]


    def column(self, index):
        rows = []
        columns = []
        for row in self.matrix_list:
            rows.append(row.split(' '))
        for row_number, row in enumerate(rows):
            for column_number, number in enumerate(row):
                try:
                    rows[row_number][column_number] = int(number)
                except ValueError:
                    print("Invalid matrix string input")
        for row_number, row in enumerate(rows):
            for column_number, number in enumerate(row):
                if column_number > len(columns) - 1:
                    columns.append([])
                columns[column_number].append(number)
        return columns[index - 1]

