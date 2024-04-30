from sys import stdin
from heapq import heappop, heappush
def way_back_home(init_y, init_x, home_y, home_x):
    
    dijk = [[2*(10**9) for _ in range(map_row + 1)] for __ in range(map_column + 1)]
    home_dijk = [[2*(10**9) for _ in range(map_row + 1)] for __ in range(map_column + 1)]
    dijk[init_y][init_x] = 0
    home_dijk[home_y][home_x] = 0
    jump_min = 2*(10**9)
    to_visit_list = list()
    from_home_list = list()
    
    heappush(from_home_list, (home_y, home_x))
    while len(from_home_list):
        cur_y, cur_x = heappop(from_home_list)
        for i in range(1, map_column+1):
            if pond[i-1][cur_x-1] == abs(cur_y - i):
                if home_dijk[cur_y][cur_x]+1 < home_dijk[i][cur_x]:
                    home_dijk[i][cur_x] = home_dijk[cur_y][cur_x]+1
                    heappush(from_home_list, (i, cur_x))
                    
        for i in range(1, map_row+1):
            if pond[cur_y-1][i-1] == abs(cur_x - i):
                if home_dijk[cur_y][cur_x]+1 < home_dijk[cur_y][i]:
                    home_dijk[cur_y][i] = home_dijk[cur_y][cur_x]+1
                    heappush(from_home_list, (cur_y, i))

    heappush(to_visit_list, (init_y, init_x))
    while len(to_visit_list):
        cur_y, cur_x = heappop(to_visit_list)
        energy = pond[cur_y - 1][cur_x - 1]
        
        dx = [energy, -energy, 0, 0]
        dy = [0, 0, energy, -energy]
        
        for i in range(4):
            x = cur_x + dx[i]
            y = cur_y + dy[i]
            if 0 < x <= map_row and 0 < y <= map_column:
                if dijk[cur_y][cur_x] + 1 < dijk[y][x]:
                    dijk[y][x] = dijk[cur_y][cur_x] + 1
                    heappush(to_visit_list, (y, x))
                    
        min_value = 2*(10**9)
        min_value_y = 0
        min_value_x = 0
        for i in range(1, map_column + 1):
            if home_dijk[i][cur_x] < min_value:
                min_value = home_dijk[i][cur_x]
                min_value_y = i
                min_value_x = cur_x
        for i in range(1, map_row + 1):
            if home_dijk[cur_y][i] < min_value:
                min_value = home_dijk[cur_y][i]
                min_value_y = cur_y
                min_value_x = i
        if min_value < 2*(10**9) and dijk[cur_y][cur_x] + 1 + home_dijk[min_value_y][min_value_x] < jump_min:
            jump_min = dijk[cur_y][cur_x] + 1 + home_dijk[min_value_y][min_value_x]

    if min(dijk[home_y][home_x], jump_min) == 2*(10**9):
        return -1
    return min(dijk[home_y][home_x], jump_min)

map_column, map_row = map(int, stdin.readline().split(' '))
init_y, init_x, home_y, home_x = map(int, stdin.readline().split(' '))
pond = list()
for _ in range(map_column):
    map_line = list(map(int, stdin.readline().split(' ')))
    pond.append(map_line)

print(way_back_home(init_y, init_x, home_y, home_x))