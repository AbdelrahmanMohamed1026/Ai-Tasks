# Dominant Value Function

import numpy as np

def dominant_eigenvalue(x):
    eigenvalues, eigenvectors = np.linalg.eig(x)
    dominant_eigenvalue = np.max(np.abs(eigenvalues))
    return dominant_eigenvalue


x = np.array([[4, 1], [2, 3]])
print("Dominant eigenvalue:", dominant_eigenvalue(x))



# 2x2 matrix
def matrix_operations(A):
    matrix_det = np.linalg.det(A)

    c = []
    for i in range(len(A)):
        for j in range(len(A[i])):
            c.append(A[i][j])

    c[0], c[3] = c[3], c[0]
    c[1], c[2] = -c[1], -c[2]
    matrix_A = np.array(c).reshape(2, 2)

    print("Determinant of matrix is", matrix_det, '\n')
    print("Cofactors matrix:", matrix_A, '\n')

    inversed_matrix = (1 / matrix_det) * matrix_A
    print("Inversed matrix:", inversed_matrix, '\n')

    identity_matrix = inversed_matrix @ A
    print("Identity matrix:", identity_matrix, '\n')


A = np.array([[2, 3], [2, 4]])
matrix_operations(A)


# 3x3 matrix using numpy

A = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print(np.linalg.inv(A))