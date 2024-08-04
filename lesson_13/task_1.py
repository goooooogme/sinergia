import random

def create_matrix(rows, cols, min_val=-50, max_val=50):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    return [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]

rows, cols = 10, 10

matrix_1 = create_matrix(rows, cols)
matrix_2 = create_matrix(rows, cols)

matrix_3 = add_matrices(matrix_1, matrix_2)

print("Matrix 1:")
for row in matrix_1:
    print(row)

print("\nMatrix 2:")
for row in matrix_2:
    print(row)

print("\nMatrix 3 (Sum of Matrix 1 and Matrix 2):")
for row in matrix_3:
    print(row)