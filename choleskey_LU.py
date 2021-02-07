import numpy as np
from scipy.linalg import lu as myfunc
from scipy.linalg import lu_solve
import math

"""
Amir Babamahmoudi  9713006
Give input to the program like this:


3
2
8
5
4
7
1
2
3
2

program gives you matrix:
2 8 5 
4 7 1 
2 3 2 

Give it vector
45
25
31


print matrix and vector:
[[2, 8, 5], [4, 7, 1], [2, 3, 2]]
[45, 25, 31]


is pos or not?
False

the deompositation:

(array([[0., 1., 0.],
       [1., 0., 0.],
       [0., 0., 1.]]), array([[ 1.        ,  0.        ,  0.        ],
       [ 0.5       ,  1.        ,  0.        ],
       [ 0.5       , -0.11111111,  1.        ]]), array([[4. , 7. , 1. ],
       [0. , 4.5, 4.5],
       [0. , 0. , 2. ]]))
       
       
       
       
final answer: 

[16.86111111 -3.83333333  4.38888889]

"""


def Cholesky_Decomposition(a, n):
    lower = [[0 for x in range(n + 1)]
             for y in range(n + 1)]

    for row in range(n):
        for col in range(row + 1):
            sum1 = 0

            if col == row:
                for k in range(col):
                    sum1 += pow(lower[col][k], 2)
                lower[col][col] = int(math.sqrt(a[col][col] - sum1))
            else:

                for k in range(col):
                    sum1 += (lower[row][k] * lower[col][k])
                if lower[col][col] > 0:
                    lower[row][col] = int((a[row][col] - sum1) /
                                          lower[col][col])

    print("Lower Triangular\t\tTranspose")
    for row in range(n):
        for col in range(n):
            print(lower[row][col], end="\t")
        print("", end="\t")

        for col in range(n):
            print(lower[col][row], end="\t")
        print("")


def fs(L, vector):
    y = []
    for i in range(len(vector)):
        y.append(vector[i])
        for j in range(i):
            y[i] = y[i] - (L[i, j] * y[j])
        y[i] = y[i] / L[i, i]

    return y


def bs(MT, y):
    x = np.zeros_like(y)

    for row in range(len(x), 0, -1):
        x[row - 1] = (y[row - 1] - np.dot(MT[row - 1, row:], x[row:])) / MT[row - 1, row - 1]

    return x


def lu_factor(A):
    L = np.zeros_like(A)
    U = np.zeros_like(A)

    N = np.size(A, 0)

    for k in range(N):
        L[k, k] = 1
        U[k, k] = (A[k, k] - np.dot(L[k, :k], U[:k, k])) / L[k, k]
        for j in range(k + 1, N):
            U[k, j] = (A[k, j] - np.dot(L[k, :k], U[:k, j])) / L[k, k]
        for i in range(k + 1, N):
            L[i, k] = (A[i, k] - np.dot(L[i, :k], U[:k, k])) / U[k, k]
    return L, U


def lu_solve(First, Second, Third):
    y = fs(First, Third)
    x = bs(Second, y)

    return x


def linear_solve(A, b):
    L, U = lu_factor(A)
    x = lu_solve(L, U, b)
    return x


if __name__ == '__main__':

    # GET Matrix
    R = int(input("enter number of rows and columns :"))
    matrix = []
    for i in range(R):
        a = []
        for j in range(R):
            a.append(int(input("type just one number and then press enter bottom:")))
        matrix.append(a)

    for i in range(R):
        for j in range(R):
            print(matrix[i][j], end=" ")
        print()

    # GET Vector
    vector = []
    for i in range(R):
        vector.append(int(input("now enter your vectors one at the time:")))
    print(matrix)
    print(vector)
    if np.all(np.linalg.eigvals(matrix) > 0):
        print("True")
        Cholesky_Decomposition(matrix, len(matrix))

        b = np.array(vector)
        a = np.array(matrix)
        print(np.linalg.solve(a, b))
    else:
        print("False")
        print(myfunc(matrix))
        P, L, U = myfunc(matrix)
        print(lu_solve(L, U, vector))
