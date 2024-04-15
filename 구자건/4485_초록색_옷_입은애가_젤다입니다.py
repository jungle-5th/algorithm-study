from sys import stdin
from collections import deque

def escape_cave(cave, cave_size):
    dijkstra_table = [[10**9 for _ in range(cave_size)] for __ in range(cave_size)]
    dijkstra_table[0][0] = cave[0][0] 
    node_need_find = deque()
    node_need_find.append((0,0))
    
    while (node_need_find):
        dx = [-1, 1, 0 ,0]
        dy = [0, 0, -1, 1]
        current_node = node_need_find.popleft()
        
        for i in range(4):
            x = current_node[1] + dy[i]
            y = current_node[0] + dx[i]
            if ((0<= x < cave_size) and (0<= y <cave_size)):
                if (dijkstra_table[current_node[0]][current_node[1]] + cave[y][x]
                                                                < dijkstra_table[y][x]):
                    dijkstra_table[y][x] = (dijkstra_table[current_node[0]][current_node[1]] 
                                                                            + cave[y][x])
                    node_need_find.append((y, x))
    return dijkstra_table[cave_size-1][cave_size-1]

test_try = 1
while(True):
    cave_size = int(stdin.readline())
    if cave_size == 0:
        break
    cave_map = list()
    for _ in range(cave_size):
        cave_line = list(map(int, stdin.readline().split(' ')))
        cave_map.append(cave_line)
    print(f"Problem {test_try}:" ,end='')
    print(escape_cave(cave_map, cave_size))
    test_try +=1