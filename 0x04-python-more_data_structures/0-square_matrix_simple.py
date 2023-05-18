#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMtrix = []
    for x in matrix:
        newMtrix.append(list(map(lambda y : y ** 2, x))) 
    return newMtrix
