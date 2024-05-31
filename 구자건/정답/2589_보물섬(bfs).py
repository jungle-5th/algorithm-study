from sys import stdin
from collections import deque

input = stdin.readline

def treasure_island():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    max_length = 0
    global visited_list
    for column in range(n_column):
        for row in range(n_row):
            if treasure_map[column][row] == "L":
                temp = [treasure_map[i].copy() for i in range(n_column)]
                bfs_que.append([column,row,0])
                temp[column][row] = "W"
                while bfs_que:
                    cur_column, cur_row, cur_length = bfs_que.popleft()
                    for i in range(4):
                        x = cur_row + dx[i]
                        y = cur_column + dy[i]
                        
                        if 0 <= x < n_row and 0 <= y < n_column and temp[y][x] == "L":
                            if dp[y][x] < cur_length + 1:
                                bfs_que.append([y, x, cur_length + 1])
                                max_length = max(max_length, cur_length + 1)
                                temp[y][x] = "W"
                                dp[y][x] = cur_length + 1
    return max_length

n_column, n_row = map(int, input().split())
treasure_map = list()
for _ in range(n_column):
    treasure_map.append(list(input().rstrip()))
dp = [[0 for i in range(n_row)] for i in range(n_column)]
bfs_que = deque()
print(treasure_island())