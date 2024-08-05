from sys import stdin
from collections import deque

input = stdin.readline
INF = 10**9
def cynical_frog():
    going_map = [[INF for i in range (row)] for j in range(column)]
    super_jumped_map = [[INF for i in range (row)] for j in range(column)]
    
    bfs.append([start_y-1, start_x-1, 0, True])
    going_map[start_y-1][start_x-1] = 0
    
    while(bfs):
        cur_y, cur_x, cur_count, super_jump_enable = bfs.popleft()
        pond_energy = pond_map[cur_y][cur_x]
        
        dx = [0, 0, -pond_energy, pond_energy]
        dy = [-pond_energy, pond_energy, 0, 0]
        
        if super_jump_enable == False:
            for i in range(4):
                x = cur_x + dx[i]
                y = cur_y + dy[i]
                if 0 <= x < row and 0 <= y < column and cur_count+1 < super_jumped_map[y][x]:
                    if y == home_y-1 and x == home_x-1:
                        return cur_count+1
                    super_jumped_map[y][x] = cur_count+1
                    bfs.append([y, x, cur_count+1, False])
        
        if super_jump_enable == True:
            for i in range(4):
                x = cur_x + dx[i]
                y = cur_y + dy[i]
                if 0 <= x < row and 0 <= y < column and cur_count+1 < going_map[y][x]:
                    if y == home_y-1 and x == home_x-1:
                        return cur_count+1
                    if cur_count+1 < super_jumped_map[y][x]:
                        super_jumped_map[y][x] = cur_count+1
                    going_map[y][x] = cur_count + 1
                    bfs.append([y, x, cur_count+1, True])
                    
            for i in range(column):
                if cur_count+1 < super_jumped_map[i][cur_x]:
                    if i == home_y-1 and cur_x == home_x-1:
                        return cur_count+1
                    super_jumped_map[i][cur_x] = cur_count+1
                    bfs.append([i, cur_x, cur_count+1, False])
                    
            for i in range(row):
                if cur_count+1 < super_jumped_map[cur_y][i]:
                    if cur_y == home_y-1 and i == home_x-1:
                        return cur_count+1
                    super_jumped_map[cur_y][i] = cur_count+1
                    bfs.append([cur_y, i, cur_count+1, False])
    return -1

column, row = map(int, input().split(" "))
start_y, start_x, home_y, home_x = map(int, input().split(' '))

pond_map = list()
for _ in range(column):
    pond_map.append(list(map(int, input().split(' '))))

bfs = deque()

print(cynical_frog())