class Matrix:
    """Object to create matrices using a string to represent the matrix."""

    def __init__(self, matrix_string: str):
        """At the init, the object transform the string in a matrix using lists.

        :param matrix_string: String representing the 05-matrix, lines separated by "\n" and rows separated by a space.
        """
        self.matrix = [[int(n) for n in line.split()] for line in matrix_string.splitlines()]

    def row(self, index: int) -> list[int]:
        """Get a row from the matrix.

        :param index: Index of the row
        :return: The row as a list
        """
        return self.matrix[index - 1]

    def column(self, index: int) -> list[int]:
        """Get a column from the matrix.

        :param index: Index of the column
        :return: The column as a list
        """
        return [line[index - 1] for line in self.matrix]
