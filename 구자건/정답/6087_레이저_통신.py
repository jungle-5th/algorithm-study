from sys import stdin
from collections import deque

input = stdin.readline

def dijk(start_row, start_column, end_row, end_column, remote_map, n_column, n_row):
    que = deque()
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    direction = [1, 2, 3, 4]

    dijk_map = [[10**9 for i in range(n_column)] for j in range(n_row)]
    
    visited_list = [[list() for i in range(n_column)] for j in range(n_row)]
    
    que.append([start_row, start_column, 0, -1])
    
    while que:
        current_row, current_column, n_mirror, direction = que.popleft()
        for i in range(4):
            y, x = current_row + dy[i], current_column + dx[i]
            if 0 <= x < n_column and 0 <= y < n_row:
                if remote_map[y][x] == '*':
                    continue
                next_n_mirror = n_mirror
                if not(direction == i or direction == -1):
                    next_n_mirror = n_mirror + 1
                if next_n_mirror <= dijk_map[y][x]:
                    if next_n_mirror < dijk_map[y][x]:
                        visited_list[y][x].clear()
                    if not i in visited_list[y][x]:
                        dijk_map[y][x] = next_n_mirror
                        que.append([y, x, next_n_mirror, i])
                        visited_list[y][x].append(i)
    return dijk_map[end_row][end_column]
    
def raiser(n_column, n_row):
    remote_map = list()
    node_list = list()
    for n in range(n_row):
        input_line = list(input().rstrip())
        for j in range(n_column):
            if input_line[j] == 'C':
                node_list.append(n)
                node_list.append(j)
        remote_map.append(input_line)
    
    start_row, start_column, end_row, end_column = node_list

    return dijk(start_row, start_column, end_row, end_column, remote_map, n_column, n_row)

n_column, n_row = map(int, input().split(' '))
print(raiser(n_column, n_row))