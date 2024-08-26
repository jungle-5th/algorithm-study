from sys import stdin
input = stdin.readline
def palindrome(n_number):
    sequence = list(map(int, input().split(' ')))
    
    dp_table = [[False for i in range(n_number + 1)] for j in range (n_number + 1)]
    for i in range(1, n_number+1):
        dp_table[i][i] = True
    
    for length in range(1, n_number):
        for i in range(1, n_number+1):
            j = i + length
            if n_number < j:
                break
            if i + 1 == j:
                dp_table[i][j] = sequence[i-1] == sequence[j-1]
                continue
            dp_table[i][j] = sequence[i-1] == sequence[j-1] and dp_table[i+1][j-1]
    
    n_question = int(input())
    for i in range(n_question):
        i,j = map(int, input().split(' '))
        if dp_table[i][j]:
            print(1)
        else: print(0)
    return

n_number = int(input())
palindrome(n_number)