from sys import stdin
from collections import deque

input = stdin.readline
INF = 10**9

def break_wall():
    if input_map[0][0] != 0: return -1
    bfs = deque()
    bfs.append([0, 0, 1, True])
    exit_map[0][0] = 1
    
    while(bfs):
        cur_y, cur_x, cur_move, break_enable = bfs.popleft()
        
        for i in range(4):
            x = cur_x + move_dx[i]
            y = cur_y + move_dy[i]
            if break_enable == True:
                if 0 <= x < row and 0 <= y <column and input_map[y][x] == 0 and exit_map[y][x] == INF:
                    exit_map[y][x] = cur_move + 1
                    bfs.append([y, x, cur_move+1, break_enable])
            if break_enable == False:
                if 0 <= x < row and 0 <= y <column and input_map[y][x] == 0 and breaked_map[y][x] == INF:
                    breaked_map[y][x] = cur_move + 1
                    bfs.append([y, x, cur_move+1, break_enable])
        
        if break_enable == True:
            for i in range(8):
                x = cur_x + break_dx[i]
                y = cur_y + break_dy[i]
                
                if 0 <= x < row and 0 <= y <column and input_map[y][x] == 0 and breaked_map[y][x] == INF:
                    breaked_map[y][x] = cur_move + 2
                    bfs.append([y, x, cur_move+2, False])
    result = min(breaked_map[column-1][row-1], exit_map[column-1][row-1])
    if result == INF: return -1
    return result

column, row = map(int, input().split(' '))
input_map = list()
for _ in range(column):
    input_map.append(list(map(int, input().rstrip())))

exit_map = [[INF for i in range(row)]for j in range(column)]
breaked_map = [[INF for i in range(row)]for j in range(column)]

move_dx = [0, 0, 1, -1]
move_dy = [1, -1, 0, 0]

break_dx = [2, -2, 0, 0, 1, 1, -1, -1]
break_dy = [0, 0, 2, -2, 1, -1, 1, -1]

print(break_wall())