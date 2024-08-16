from sys import stdin, stdout
from collections import deque
import copy
input = stdin.readline
print = stdout.write
def ice_meltdown(visited_list, ice_list, n_column, n_row):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    melt_list = list()
    for ice in range(len(ice_list)):
        ice_column, ice_row = ice_list[ice]
        for i in range(4):
            around_column, around_row = ice_column + dy[i], ice_row + dx[i]
            if 0 <= around_column < n_column and 0 <= around_row < n_row and visited_list[around_column][around_row] == False:
                melt_list.append([ice_list[ice][0], ice_list[ice][1], ice])
                break
    for ice in range(len(melt_list)):
        ice_column, ice_row, ice_index = melt_list[-1-ice]
        visited_list[ice_column][ice_row] = False
        ice_list.pop(ice_index)
    return

def swan_lake(n_column, n_row):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited_list = [[False for i in range(n_row)] for j in range(n_column)]
    swan_list = list()
    ice_list = list()
    
    for i in range(n_column):
        input_line = list(input().rstrip())
        for j in range(n_row):
            if input_line[j] == 'X':
                visited_list[i][j] = True
                ice_list.append([i, j])
            if input_line[j] == 'L':
                swan_list.append(i)
                swan_list.append(j)
    bfs = deque()
    start_column, start_row = swan_list[0], swan_list[1]
    target_column, target_row = swan_list[2], swan_list[3]
    time = 0
    while True:
        temp = copy.deepcopy(visited_list)
        bfs.append([start_column, start_row])
        temp[start_column][start_row] = True
        while bfs:
            cur_column, cur_row = bfs.popleft()
            for i in range(4):
                next_column, next_row = cur_column + dy[i], cur_row + dx[i]
                if next_column == target_column and next_row == target_row:
                    return time
                
                if 0 <= next_column < n_column and 0 <= next_row < n_row and temp[next_column][next_row] == False:
                    bfs.append([next_column, next_row])
                    temp[next_column][next_row] = True
        ice_meltdown(visited_list, ice_list, n_column, n_row)
        time += 1

n_column, n_row = map(int, input().split(' '))
print(swan_lake(n_column, n_row))