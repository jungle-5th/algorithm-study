from sys import stdin
from collections import deque
def cynical_frog(start_y, start_x, home_y, home_x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    if start_y == home_y and start_x == home_x:
        return 0
    
    bfs_list = deque()
    bfs_list.append((start_y, start_x, 0, True))
    
    while bfs_list:
        cur_y , cur_x, move, super_jump_enable = bfs_list.popleft()
        pond_energy = pond[cur_y][cur_x]
        visited_map[cur_y][cur_y] = True
        for i in range(4):
            x = cur_x + (dx[i]*pond_energy)
            y = cur_y + (dy[i]*pond_energy)
            
            if 0 <= x < map_x and 0 <= y < map_y and visited_map[y][x] == False:
                if y == home_y and x == home_x:
                    return move + 1
                bfs_list.append((y, x, move+1, super_jump_enable))
                visited_map[y][x] = True
                
        if super_jump_enable == True:
            for i in range(0, map_x):
                if jump_visited_map[cur_y][i] == False:
                    if cur_y == home_y and i == home_x:
                        return move + 1
                    bfs_list.append((cur_y, i, move+1, False))
                    jump_visited_map[cur_y][i] = True
                    
            for i in range(0, map_y):
                if jump_visited_map[i][cur_x] == False:
                    if i == home_y and cur_x == home_x:
                        return move + 1
                    bfs_list.append((i, cur_x, move+1, False))
                    jump_visited_map[i][cur_x] = True
    
    return -1

map_y, map_x = map(int, stdin.readline().split(' '))
start_y, start_x, home_y, home_x = map(int, stdin.readline().split(' '))
pond = list()
visited_map = [[False for _ in range(map_x)]for __ in range(map_y)]
jump_visited_map = [[False for _ in range(map_x)]for __ in range(map_y)]
for _ in range(map_y):
    pond.append(list(map(int, stdin.readline().split(' '))))

print(cynical_frog(start_y-1, start_x-1, home_y-1, home_x-1))