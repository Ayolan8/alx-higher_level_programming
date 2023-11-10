#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lamba y: y * y, row)) for row in matrix]) 
