from sys import stdin
from collections import deque

input = stdin.readline

def do_bfs(bfs, sea_map, n_row, n_column):
    while bfs:
        cur_y, cur_x = bfs.popleft()
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                bfs_x = cur_x + dx
                bfs_y = cur_y + dy
                
                if 0 <= bfs_x < n_row and 0 <= bfs_y < n_column:
                    if sea_map[bfs_y][bfs_x] == 1:
                        sea_map[bfs_y][bfs_x] = 0
                        bfs.append([bfs_y, bfs_x])
    return 


def find_island(sea_map, bfs):
    count = 0
    for y in range (n_column):
        for x in range(n_row):
            if sea_map[y][x] == 1:
                sea_map[y][x] = 0
                bfs.append([y, x])
                count += 1
                do_bfs(bfs, sea_map, n_row, n_column)
    return count


def number_of_island(n_column, n_row):
    sea_map = list()
    for _ in range(n_column):
        sea_map.append(list(map(int, input().split(' '))))
    
    bfs = deque()
    
    return find_island(sea_map, bfs)


while True:
    
    n_row , n_column = map(int, input().split(' '))
    if n_row == 0 : break
    print(number_of_island(n_column, n_row))