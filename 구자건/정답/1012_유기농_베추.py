from sys import stdin
from collections import deque

input = stdin.readline

def wellbeing_napa_cabbage(n_rows, n_columns, n_cabbages):
    field_map = [[0 for i in range(n_rows)] for j in range(n_columns)]
    bug_count = 0
    bfs_queue = deque()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(n_cabbages):
        x, y = map(int, input().split(' '))
        field_map[y][x] = 1
    
    for i in range(n_columns):
        for j in range(n_rows):
            if field_map[i][j] == 1:
                bfs_queue.append([i, j])
                bug_count += 1
                while bfs_queue:
                    cur_y, cur_x = bfs_queue.popleft()
                    for k in range(4):
                        x = cur_x + dx[k]
                        y = cur_y + dy[k]
                        if 0 <= x < n_rows and 0 <= y < n_columns:
                            if field_map[y][x] == 1:
                                field_map[y][x] = 0
                                bfs_queue.append([y, x])
    print(bug_count)
    return

n_tries = int(input())

for _ in range(n_tries):
    n_rows, n_columns, n_cabbages = map(int, input().split(' '))
    wellbeing_napa_cabbage(n_rows, n_columns, n_cabbages)