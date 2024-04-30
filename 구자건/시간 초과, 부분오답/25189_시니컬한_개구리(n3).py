from sys import stdin
from heapq import heappop, heappush
def way_back_home(init_y, init_x, home_y, home_x):
    
    dijk = [[2*(10**9) for _ in range(map_row + 1)] for __ in range(map_column + 1)]
    shortcuted_dijk = [[2*(10**9) for _ in range(map_row + 1)] for __ in range(map_column + 1)]
    dijk[init_y][init_x] = 0
    shortcuted_dijk[init_y][init_x] = 0
    
    to_visit_list = list()
    heappush(to_visit_list, (init_y, init_x, True))
    
    while len(to_visit_list):
        cur_y, cur_x, shortcut_enable = heappop(to_visit_list)
        energy = pond[cur_y - 1][cur_x - 1]
        
        dx = [energy, -energy, 0, 0]
        dy = [0, 0, energy, -energy]
        if not shortcut_enable:
            for i in range(4):
                x = cur_x + dx[i]
                y = cur_y + dy[i]
                if 0< x <= map_row and 0 < y <= map_column:
                    if shortcuted_dijk[cur_y][cur_x] + 1 < shortcuted_dijk[y][x]:
                        shortcuted_dijk[y][x] = shortcuted_dijk[cur_y][cur_x] + 1
                        heappush(to_visit_list, (y, x, False))
        
        if shortcut_enable:
            for i in range(4):
                x = cur_x + dx[i]
                y = cur_y + dy[i]
                if 0< x <= map_row and 0 < y <= map_column:
                    if dijk[cur_y][cur_x] + 1 < dijk[y][x]:
                        dijk[y][x] = dijk[cur_y][cur_x] + 1
                        heappush(to_visit_list, (y, x, True))
                        
            for i in range(1, map_column+1):
                if dijk[cur_y][cur_x] + 1 < shortcuted_dijk[i][cur_x]:
                    shortcuted_dijk[i][cur_x] = dijk[cur_y][cur_x] + 1
                    heappush(to_visit_list, (i, cur_x, False))
                    
            for i in range(1, map_row+1):
                if dijk[cur_y][cur_x] + 1 < shortcuted_dijk[cur_y][i]:
                    shortcuted_dijk[cur_y][i] = dijk[cur_y][cur_x] + 1
                    heappush(to_visit_list, (cur_y, i, False))
    
    if 2*(10**9) == min(dijk[home_y][home_x], shortcuted_dijk[home_y][home_x]):
        return -1
    return min(dijk[home_y][home_x], shortcuted_dijk[home_y][home_x])

map_column, map_row = map(int, stdin.readline().split(' '))
init_y, init_x, home_y, home_x = map(int, stdin.readline().split(' '))
pond = list()
for _ in range(map_column):
    map_line = list(map(int, stdin.readline().split(' ')))
    pond.append(map_line)

print(way_back_home(init_y, init_x, home_y, home_x))