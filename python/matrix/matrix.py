class Matrix:
    rows = []
    columns = []

    def __init__(self, matrix_string):
        self.rows = matrix_string.split("\n")
        for row_number, row in enumerate(self.rows):
            self.rows[row_number] = row.split(' ')
        for row_number, row in enumerate(self.rows):
            for column_number, number in enumerate(row):
                try:
                    self.rows[row_number][column_number] = int(number)
                except ValueError:
                    print("Invalid matrix string input")
        for row_number, row in enumerate(self.rows):
            for column_number, number in enumerate(row):
                if column_number > len(self.columns) - 1:
                    self.columns.append([])
                self.columns[column_number].append(number)


    def row(self, index):
        return self.rows[index - 1]


    def column(self, index):
        return self.columns[index - 1]