from sys import stdin

def flower_road(column, row, seed, cost):
    global min_cost
    if seed == 3:
        min_cost = min(min_cost, cost)
        return
    global enable_seed
    for i in range(column, length):
        for j in range(row, length):
            if enable_seed[i][j] and 0 < i < length-1 and 0 < j < length-1:
                temp = [[enable_seed[__][_] for _ in range(length)]for __ in range(length)]
                cur_cost = cost
                for k in range(13):
                    y = i + dy[k]
                    x = j + dx[k]
                    if 0 <= y < length and 0 <= x < length:
                        enable_seed[y][x] = False
                for k in range(5):
                    y = i + cost_dy[k]
                    x = j + cost_dx[k]
                    cur_cost += garden[y][x]
                flower_road(column, row, seed+1, cur_cost)
                enable_seed = [[temp[__][_] for _ in range(length)]for __ in range(length)]
    return
dx = [-2, 2, 0, 0, -1, 0, 1, -1, 0, 1, -1, 0 ,1]
dy = [0, 0, -2, 2, -1, -1, -1, 0, 0, 0, 1, 1, 1]
cost_dx = [-1, 1, 0, 0, 0]
cost_dy = [0, 0, -1, 1, 0]

length = int(stdin.readline())
garden = [list(map(int, stdin.readline().split(' '))) for _ in range(length)]
enable_seed = [[True for _ in range(length)]for __ in range(length)]
min_cost = 10**9
flower_road(0, 0, 0, 0)

print(min_cost)