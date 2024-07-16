from sys import stdin
from collections import deque
input = stdin.readline

def find_friend(n_column, n_row):
    school_map = list()
    start_column, start_row = 0, 0
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(n_column):
        map_line = list(input().rstrip())
        if 'I' in map_line:
            j = map_line.index('I')
            start_column, start_row = i, j
        school_map.append(map_line)
    
    bfs = deque()
    bfs.append([start_column, start_row])
    school_map[start_column][start_row] = 'X'
    count = 0
    while(bfs):
        cur_y, cur_x = bfs.popleft()
        
        for i in range(4):
            x = cur_x + dx[i]
            y = cur_y + dy[i]
            
            if 0 <= x < n_row and 0 <= y < n_column:
                if school_map[y][x] == 'O':
                    bfs.append([y, x])
                    school_map[y][x] = 'X'
                if school_map[y][x] == 'P':
                    bfs.append([y, x])
                    school_map[y][x] = 'X'
                    count += 1
    if count == 0:
        return 'TT'
    return count

n_column, n_row = map(int, input().split(' '))

print(find_friend(n_column, n_row))