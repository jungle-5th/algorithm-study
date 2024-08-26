from sys import stdin
input = stdin.readline

def zoac(n_row, n_column, d_row, d_column):
    return (1 + ((n_row-1) // (d_row + 1))) * (1 + ((n_column-1) // (d_column + 1)))

n_row, n_column, d_row, d_column = map(int, input().split(' '))

print(zoac(n_row, n_column, d_row, d_column))