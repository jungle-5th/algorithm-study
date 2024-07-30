from sys import stdin
from collections import deque
input = stdin.readline

def make_matrix(matrix_size):
    number_column = list(map(int, input().split()))
    number_row = list(map(int, input().split()))
    matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
    adj_list = [[[] for _ in range(matrix_size)] for _ in range(4)]
    
    for i in range(matrix_size):
        adj_list[0][0].append((1, i))
    for i in range(matrix_size):
        for j in range(matrix_size):
            adj_list[1][i].append((2, j))
    for i in range(matrix_size):
        adj_list[2][i].append((3, 0))
    
    while True:
        bfs = deque()
        bfs.append([(0, 0)])
        route_exist = False
        while bfs:
            cur_route = bfs.popleft()
            for next in adj_list[cur_route[-1][0]][cur_route[-1][1]]:
                if next[0] == 1:
                    if number_column[next[1]] > 0:
                        next_route = cur_route.copy()
                        next_route.append(next)
                        bfs.append(next_route)
                elif next[0] == 2:
                    if number_row[next[1]] > 0:
                        if matrix[cur_route[-1][1]][next[1]] == 0:
                            matrix[cur_route[-1][1]][next[1]] = 1
                            route_exist = True
                            number_column[cur_route[-1][1]] -= 1
                            number_row[next[1]] -= 1
                            bfs.clear()
                            break
        if not route_exist:
            break
    
    if sum(number_column) != 0 or sum(number_row) != 0:
        print(-1)
        return
    
    print(1)
    for row in matrix:
        print(*row)
    return

matrix_size = int(input())
make_matrix(matrix_size)
