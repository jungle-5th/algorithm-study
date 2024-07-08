from sys import stdin
input = stdin.readline
def sum_mex(n_number):
    a_list = list(map(int, input().split(' ')))
    a_list.sort()
    count = 0
    sum_zero = 0
    sum_one = 0
    sum_else = 0
    zero_count = 0
    for i in range(n_number):
        if a_list[i] == 1:
            sum_zero += 2
        else: sum_zero += 1
    for i in range(n_number):
        if a_list[i] == 0:
            sum_zero -= 1
            count += sum_zero
    
    return count

n_number = int(input())

print(sum_mex(n_number))
