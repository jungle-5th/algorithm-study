from sys import stdin
from collections import deque
input = stdin.readline


# 불: -1, 벽:0, 경로: 1 상근이:2
def escape_building():
    n_row, n_column = map(int, input().split(' '))
    building_map = list()
    start_y = -1
    start_x = -1
    
    exit_y = -1
    exit_x = -1
    for y in range(n_column):
        input_line = list(input().rstrip())
        map_line = list()
        for x in range(n_row):
            if input_line[x] == '#':
                map_line.append(0)
                
            if input_line[x] == '*':
                map_line.append(-1)
                fire_bfs.append([y, x, 0])
                
            if input_line[x] == '.':
                map_line.append(1)
                    
            if input_line[x] == '@':
                map_line.append(2)
                sg_bfs.append([y, x, 0])
                
        building_map.append(map_line)
    
    return simulator(building_map, exit_y, exit_x, n_column, n_row, fire_bfs, sg_bfs)

def simulator(building_map, exit_y, exit_x, n_column, n_row, fire_bfs, sg_bfs):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    time = 0
    while(sg_bfs):
        while(fire_bfs and fire_bfs[0][2] <= time) :
            cur_fire_y, cur_fire_x, cur_time = fire_bfs.popleft()
            for i in range(4):
                y = cur_fire_y + dy[i]
                x = cur_fire_x + dx[i]
                if 0 <= x < n_row and 0 <= y < n_column:
                    if building_map[y][x] > 0:
                        if y == exit_y and x == exit_x:
                            return "IMPOSSIBLE"
                        building_map[y][x] = -1
                        fire_bfs.append([y, x, cur_time+1])

        while(sg_bfs and sg_bfs[0][2] <= time) :
            cur_sg_y, cur_sg_x, cur_time = sg_bfs.popleft()
            if cur_sg_x == 0 or cur_sg_y == 0 or cur_sg_x == n_row-1 or cur_sg_y == n_column-1:
                return cur_time + 1
            for i in range(4):
                y = cur_sg_y + dy[i]
                x = cur_sg_x + dx[i]
                if 0 <= x < n_row and 0 <= y < n_column and building_map[y][x] == 1:
                    building_map[y][x] = 2
                    sg_bfs.append([y, x, cur_time+1])
        time += 1
    return "IMPOSSIBLE"

buildings = int(input())
for t in range(buildings):
    fire_bfs = deque()
    sg_bfs = deque()
    print(escape_building())