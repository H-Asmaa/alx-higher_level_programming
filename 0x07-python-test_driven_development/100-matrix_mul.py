#!/usr/bin/python3
"""matrix_mul function"""


def matrix_mul(m_a, m_b):
    """
        A function that does the multiplication of two matrix

        Returns :
                new_matrix

        Raises :
                TypeError
        """
    lines_m_a = 0
    lines_m_b = 0
    cols_m_a = 0
    cols_m_b = 0
    matrix_mul = []
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for item in m_a:
        if not isinstance(item, list):
            raise TypeError("m_a must be a list of lists")
    for item in m_b:
        if not isinstance(item, list):
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        cols_m_a += 1
        for j in i:

            if not isinstance(j, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        cols_m_b += 1
        for j in i:

            if not isinstance(j, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    for i in range(len(m_a)):
        lines_m_a += 1
        if i < len(m_a) - 1 and len(m_a[i]) != len(m_a[i + 1]):
            raise TypeError("each row of m_a must be of the same size")
    for i in range(len(m_b)):
        lines_m_b += 1
        if i < len(m_b) - 1 and len(m_b[i]) != len(m_b[i + 1]):
            raise TypeError("each row of m_b must be of the same size")
    if cols_m_a != lines_m_b:
        raise ValueError("m_a and m_b can't be multiplied")
    i = 0
    new_matrix = []
    while (i < cols_m_a):
        new_matrix[i] = matrix_mul[i] * matrix_mul[]
    line_b = 0
    col_b = 0
    for i in m_a:
        for j in i:
            matrix_mul.append(j*m_b[line_b][col_b])
            line_b += 1
        col_b += 1
    print(matrix_mul)



    # lines of m_a will be multiplied by cols of m_b
    line_b = 0
    col_b = 0
    for i in m_a:
        if col_b == cols_m_b:
            break
        for j in i:
            if line_b == lines_m_b:
                break
            matrix_mul.append(j*m_b[line_b][col_b])
            line_b += 1
        col_b += 1
    print(matrix_mul)


print(matrix_mul(
    [
        [1, 2],
        [3, 4]
    ],
    [
        [1, 2],
        [3, 4]
    ]
))

"""    i = 0
    commun = 0

    while(i < cols_m_a):
        for j in m_b:
        m_a[0][commun] * m_b[commun][0]


"""
