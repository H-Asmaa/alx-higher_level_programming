#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_copy = [row[:] for row in matrix]
    for i in range(len(matrix_copy)):
        for j in range(len(matrix_copy[i])):
            matrix_copy[i][j] = matrix_copy[i][j] ** 2
    return matrix_copy
