from sys import stdin
input = stdin.readline
def sum_mex(n_number):
    a_list = list(map(int, input().split(' ')))
    a_list.sort()
    count = 0
    sum_zero = 0
    one_count = 0
    for i in range(n_number):
        if a_list[i] == 1:
            one_count += 1
        if a_list[i] > 1:
            break
    sum_zero += one_count*2 + (n_number-one_count)
    for i in range(n_number):
        if a_list[i] == 0:
            sum_zero -= 1
            count += sum_zero
        if a_list[i] != 0: break
    return count

n_number = int(input())

print(sum_mex(n_number))
