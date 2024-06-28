from sys import stdin

input = stdin.readline

def cow(n_cow, n_trick):
    cow_value_list = list(map(int, input().split(' ')))
    trick_list = list(map(int, input().split(' ')))
    c_list = cow_value_list + cow_value_list[0:4]
    
    value_list = list()
    total_value = 0
    
    for i in range(n_cow):
        value = 1
        for j in range(4):
            value = value*c_list[i+j]
        value_list.append(value)
        total_value += value
    
    for i in range(n_trick):
        trick_target = trick_list[i]-1
        for j in range(4):
            value_list[trick_target-j] = -value_list[trick_target-j]
            total_value += 2*(value_list[trick_target-j])
        print(total_value)
    return

n_cow, n_trick = map(int, input().split(' '))
cow(n_cow, n_trick)