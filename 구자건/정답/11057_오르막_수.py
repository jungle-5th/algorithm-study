from sys import stdin
input = stdin.readline


def uprising_number():
    uprising_table = [[0 for __ in range(10)] for _ in range (n_number)]
    for i in range(10):
        uprising_table[0][i] = 1
    for i in range (n_number-1):
        for j in range(10):
            for k in range(j+1):
                uprising_table[i+1][k] += uprising_table[i][j]
    if sum(uprising_table[n_number - 1]) > 10007:
        return sum(uprising_table[n_number - 1]) % 10007
    return sum(uprising_table[n_number - 1])


n_number = int(input())

print(uprising_number())