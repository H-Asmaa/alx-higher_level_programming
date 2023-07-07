#!/usr/bin/python3
"""matrix_devided function"""


def matrix_divided(matrix, div):
    """
    Function that performs devision of a matrix.

    Returns :
        new_matrix the matrix devided by dev

    Raises :
        TypeError in case the elements are not int nor float
        TypeError in case the rows of the matrix are not the same size
        TypeError in case div is not int nor float
        ZeroDivisionError in case the div is equals to zero
    """
    new_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
        if i < len(matrix) - 1 and len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        tmp = []
        for j in range(len(matrix[i])):
            division = round(matrix[i][j] / div, 2)
            tmp.append(division)
        new_matrix.append(tmp)
    return new_matrix
