#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
     """
    A function that computes the square
    value of all integers of a matrix.
    """
    new_matrix = []
    for col in matrix:
        for x in col:
            result = x**2
            new_matrix.append(result)
    return new_matrix
