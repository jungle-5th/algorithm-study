from sys import stdin
from collections import deque
input = stdin.readline

def move(ball_map, r_column, r_row, b_column, b_row, g_column, g_row, dx, dy):
    move = True
    next_r_column, next_r_row, next_b_column, next_b_row = r_column, r_row, b_column, b_row

    while move:
        move = False
        if ball_map[next_r_column + dy][next_r_row + dx] == '.' or ball_map[next_r_column + dy][next_r_row + dx] == 'O':
            if ball_map[next_r_column + dy][next_r_row + dx] == 'O':
                move = True
                next_r_column = next_r_column + dy
                next_r_row = next_r_row + dx
            elif (next_r_column + dy != next_b_column or next_r_row + dx != next_b_row) and (next_r_column != g_column or next_r_row != g_row):
                move = True
                next_r_column = next_r_column + dy
                next_r_row = next_r_row + dx
            
        if ball_map[next_b_column + dy][next_b_row + dx] == '.' or ball_map[next_b_column + dy][next_b_row + dx] == 'O':
            if ball_map[next_b_column + dy][next_b_row + dx] == 'O':
                move = True
                next_b_column = next_b_column + dy
                next_b_row = next_b_row + dx
            elif (next_b_column + dy != next_r_column or next_b_row + dx != next_r_row) and (next_b_column != g_column or next_b_row != g_row):
                move = True
                next_b_column = next_b_column + dy
                next_b_row = next_b_row + dx

    return next_r_column, next_r_row, next_b_column, next_b_row

def ball_escape(n_column, n_row):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    r_column, r_row, b_column, b_row, g_column, g_row = 0, 0, 0, 0, 0, 0
    bfs = deque()
    ball_map = list()
    visited_list = list()
    for i in range(n_column):
        input_line = list(input().rstrip())
        if 'R' in input_line:
            r_column, r_row = i, input_line.index('R')
            input_line[input_line.index('R')] = '.'
        if 'B' in input_line:
            b_column, b_row = i, input_line.index('B')
            input_line[input_line.index('B')] = '.'
        if 'O' in input_line:
            g_column, g_row = i, input_line.index('O')
        ball_map.append(input_line)
        
    bfs.append([r_column, r_row, b_column, b_row, 0])
    
    while bfs:
        cur_r_column, cur_r_row, cur_b_column, cur_b_row, cur_count = bfs.popleft()
        if 10 <= cur_count: return -1
        for i in range(4):
            next_r_column, next_r_row, next_b_column, next_b_row = move(
                ball_map, cur_r_column, cur_r_row, cur_b_column, cur_b_row, g_column, g_row, dx[i], dy[i]
                )
            if next_r_column == g_column and next_r_row == g_row:
                if next_b_column != g_column or next_b_row != g_row:
                    return cur_count + 1
            if not [next_r_column, next_r_row, next_b_column, next_b_row] in visited_list:
                if next_b_column != g_column or next_b_row != g_row:
                    bfs.append([next_r_column, next_r_row, next_b_column, next_b_row, cur_count + 1])
                    visited_list.append([next_r_column, next_r_row, next_b_column, next_b_row])
    return -1

n_column, n_row = map(int, input().split(' '))
print(ball_escape(n_column, n_row))