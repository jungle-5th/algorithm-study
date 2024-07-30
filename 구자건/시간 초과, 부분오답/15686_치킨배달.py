from sys import stdin
input = stdin.readline

def find_chicken_range(home_list, chicken_list, cur_chicken_list, n_chicken, index):
    if len(cur_chicken_list) == n_chicken:
        range_list = [10**9 for i in range(len(home_list))]
        for i in range(n_chicken):
            for j in range(len(home_list)):
                range_list[j] = min(range_list[j], abs(cur_chicken_list[i][0]-home_list[j][0])+abs(cur_chicken_list[i][1]-home_list[j][1]))
        return sum(range_list)
    min_sum_range = 10**9
    for i in range(index, len(chicken_list)):
        next_chicken_list = cur_chicken_list.copy()
        next_chicken_list.append(chicken_list[i])
        min_sum_range = min(min_sum_range, find_chicken_range(home_list, chicken_list, next_chicken_list, n_chicken, i+1))
    
    return min_sum_range

def chicken_delivery(map_size, n_chicken):
    home_list = list()
    chicken_list = list()
    for i in range(map_size):
        input_line = list(map(int, input().split(' ')))
        for j in range(map_size):
            if input_line[j] == 1:
                home_list.append([i, j])
            if input_line[j] == 2:
                chicken_list.append([i, j])
    return find_chicken_range(home_list, chicken_list,list(), n_chicken, 0)

map_size, n_chicken = map(int, input().split(' '))

print(chicken_delivery(map_size, n_chicken))