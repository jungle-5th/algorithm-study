from sys import stdin
input = stdin.readline

def file_merge(n_file):
    dp_table = [[10**9 for i in range(n_file)]for j in range(n_file)]
    file_list = list(map(int, input().split(' ')))
    for i in range(n_file):
        dp_table[i][i] = file_list[i]
    
    for i in range(1, n_file):
        min_value = dp_table[0][i-1] + dp_table[i][i]
        for j in range(i):
            dp_min = 10**9
            for k in range(j+1):
                dp_min = min(dp_min, 2*dp_table[i-k][i] + 2*dp_table[i-1-j][i-1-k])
            dp_table[i-1-j][i] = dp_min
    return

n_book = int(input())
for i in range(n_book):
    n_file = int(input())
    file_merge(n_file)