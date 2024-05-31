from sys import stdin
INF = 10**9
input = stdin.readline

def treasure_island():
    max_length = 0
    seek_points = row*column
    for i in range(seek_points):
        for j in range(seek_points):
            for k in range(seek_points):
                treasure_map[j][k] = min(treasure_map[j][k], treasure_map[j][i]+treasure_map[i][k])
    for i in range(seek_points):
        for j in range(seek_points):
            if treasure_map[i][j] != INF and max_length < treasure_map[i][j]:
                max_length = treasure_map[i][j]

    return max_length

column, row = map(int, input().split())
treasure_map = [[INF for _ in range(row*column)] for __ in range(row*column)]
seek_points = row*column
dx = [-1, 0]
dy = [0, -1]

input_map = list()
for _ in range(column):
    column_line = list(input().rstrip())
    input_map.append(column_line)

for i in range(seek_points):
    seek_column = i//row
    seek_row = i%column
    if input_map[seek_column][seek_row] == "L":
        for j in range(2):
            y = seek_column + dy[j]
            x = seek_row + dx[j]
            if 0 <= x < row and 0 <= y < column:
                if input_map[y][x] == "L":
                    seek_point = (y*row)+x
                    treasure_map[seek_point][i] = 1
                    treasure_map[i][seek_point] = 1

for _ in range(seek_points):
    seek_column = _//row
    seek_row = _%column
    if input_map[seek_column][seek_row] == "L":
        treasure_map[_][_] = 0
    else: treasure_map[_][_] = INF
    
print(treasure_island())