from sys import stdin
input = stdin.readline
def make_drink():
    max_sum = 0
    max_sum += drink_list[n_drink-1]
    
    for i in range(n_drink -1):
        max_sum = max(max_sum, drink_list[i]) + (min(max_sum, drink_list[i])/2)
    
    return max_sum

n_drink = int(input())
drink_list = list(map(int, input().split(' ')))
drink_list.sort()

print(make_drink())