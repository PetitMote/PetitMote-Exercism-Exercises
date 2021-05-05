class Matrix:
    """Object to create matrices using a string to represent the 05-matrix"""

    def __init__(self, matrix_string: str):
        """At the init, the object transform the string in a 05-matrix using lists

        :param matrix_string: String representing the 05-matrix, lines separated by "\n" and rows separated by a space.
        """
        lines_strings = matrix_string.splitlines()
        self.matrix = [line.split(" ") for line in lines_strings]
        for i in range(0, len(self.matrix)):
            self.matrix[i] = [int(n) for n in self.matrix[i]]

    def row(self, index: int) -> list[int]:
        """Get a row from the 05-matrix

        :param index: Index of the row
        :return: The row as a list
        """
        return self.matrix[index - 1]

    def column(self, index: int) -> list[int]:
        """Get a column from the 05-matrix

        :param index: Index of the column
        :return: The column as a list
        """
        column: list[int] = []
        for line in self.matrix:
            column.append(line[index - 1])
        return column
