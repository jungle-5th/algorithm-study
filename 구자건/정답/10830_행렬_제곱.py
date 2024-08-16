from sys import stdin
import copy
input = stdin.readline

def square(matrix, matrix_size):
    new_matrix = list()
    for i in range (matrix_size):
        matrix_line = list()
        for j in range(matrix_size):
            number = 0
            for k in range(matrix_size):
                number += matrix[i][k] * matrix[k][j]
            if 1000 <= number:
                number %= 1000
            matrix_line.append(number)
        new_matrix.append(matrix_line)
        
    return new_matrix

def complex(matrix1, matrix2, matrix_size):
    new_matrix = list()
    for i in range (matrix_size):
        matrix_line = list()
        for j in range(matrix_size):
            number = 0
            for k in range(matrix_size):
                number += matrix1[i][k] * matrix2[k][j]
            if 1000 <= number:
                number %= 1000
            matrix_line.append(number)
        new_matrix.append(matrix_line)
        
    return new_matrix

def matrix_square(matrix_size, n_square):
    original_matrix = list()
    answer_matrix = [[ 1 if j == i else 0 for i in range(matrix_size)] for j in range(matrix_size)]
    for i in range(matrix_size):
        original_matrix.append(list(map(int, input().split(' '))))
    
    binary_n_square = list(map(int,format(n_square, 'b')))
    binary_n_square.reverse()
    for i in range(len(binary_n_square)):
        if binary_n_square[i]:
            answer_matrix = complex(answer_matrix, original_matrix, matrix_size)
        original_matrix = square(original_matrix, matrix_size)
    for i in answer_matrix:
        print(*i)
    return

matrix_size, n_square = map(int, input().split(' '))
matrix_square(matrix_size, n_square)