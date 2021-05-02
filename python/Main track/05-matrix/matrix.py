def separate_lines(matrix_string: str) -> list[str]:
    """Separate the lines of a matrix represented as a String

    :param matrix_string: A matrix as a string, lines separated by "\n"
    :return: A list of strings, each string being a line of the matrix
    """
    lines_strings = []
    newline = matrix_string.find("\n")
    while newline != -1:
        lines_strings.append(matrix_string[:newline])
        matrix_string = matrix_string[newline + 1:]
        newline = matrix_string.find("\n")
    lines_strings.append(matrix_string)
    return lines_strings


def separate_rows(line_string: str) -> list[int]:
    """Separate the rows of a line from a matrix, represented as a String

    :param line_string: Line of a matrix, each row separated by a space
    :return: A list of ints, each int being one row of the line
    """
    rows: list[int] = []
    space = line_string.find(" ")
    while space != -1:
        rows.append(int(line_string[:space]))
        line_string = line_string[space + 1:]
        space = line_string.find(" ")
    rows.append(int(line_string))
    return rows


class Matrix:
    """Object to create matrices using a string to represent the matrix"""

    def __init__(self, matrix_string: str):
        """At the init, the object transform the string in a matrix using lists

        :param matrix_string: String representing the matrix, lines separated by "\n" and rows separated by a space.
        """
        self.matrix = []
        lines_strings = separate_lines(matrix_string)
        for line in lines_strings:
            self.matrix.append(separate_rows(line))

    def row(self, index: int) -> list[int]:
        """Get a row from the matrix

        :param index: Index of the row
        :return: The row as a list
        """
        return self.matrix[index - 1]

    def column(self, index: int) -> list[int]:
        """Get a column from the matrix

        :param index: Index of the column
        :return: The column as a list
        """
        column: list[int] = []
        for line in self.matrix:
            column.append(line[index - 1])
        return column
