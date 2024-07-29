from sys import stdin
from collections import deque
input = stdin.readline

def find_matrix(matrix_size):
    matrix = [[0 for i in range(matrix_size)]for j in range(matrix_size)]
    n_true_in_column = list(map(int, input().split(' ')))
    n_true_in_row = list(map(int, input().split(' ')))
    column_value_set = list()
    row_value_set = list()
    if sum(n_true_in_column) != sum(n_true_in_row):
        print(-1)
        return
    
    for i in range (matrix_size):
        column_value_set.append([n_true_in_column[i], i])
    for i in range (matrix_size):
        row_value_set.append([n_true_in_row[i], i])
    column_value_set.sort(reverse= True)
    row_value_set.sort(reverse= True)
    column_value_set = deque(column_value_set)
    row_value_set = deque(row_value_set)
    
    while column_value_set:
        column_value, column = column_value_set.popleft()
        for i in range(column_value):
            if not row_value_set:
                print(-1)
                return
            row_value, row = row_value_set.popleft()
            if matrix[column][row] == 0:
                matrix[column][row] = 1
                column_value -= 1
                row_value -= 1
            if 0 < row_value:
                row_value_set.append([row_value, row])
        if 0 < column_value:
            column_value_set.append([column_value, column])
    print (1)
    for i in matrix:
        print(*i)
    return


matrix_size = int(input())
find_matrix(matrix_size)