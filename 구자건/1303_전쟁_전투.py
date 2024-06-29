from sys import stdin
from collections import deque
input = stdin.readline

def warfare(n_rows, n_columns):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    white = 0
    black = 0
    battle_field = list()
    visited_list = [[False for _ in range(n_rows)]for __ in range(n_columns)]

    for column in range(n_columns):
        battle_field.append(list(input().rstrip()))

    bfs = deque()
    for column in range(n_columns):
        for row in range(n_rows):
            if visited_list[column][row] == False:
                value = battle_field[column][row]
                visited_list[column][row] = True
                cluster_size = 1
                bfs.append([column, row])
                
                while bfs:
                    cur_y, cur_x = bfs.popleft()
                    for i in range(4):
                        x = cur_x + dx[i]
                        y = cur_y + dy[i]
                        
                        if 0 <= x < n_rows and 0 <= y < n_columns and visited_list[y][x] == False and battle_field[y][x] == value:
                            visited_list[y][x] = True
                            cluster_size += 1
                            bfs.append([y, x])
                if value == 'W':
                    white += (cluster_size**2)
                else:
                    black += (cluster_size**2)
    print(white, end=' ')
    print(black)
    return

n_rows, n_columns = map(int, input().split(' '))
warfare(n_rows, n_columns)