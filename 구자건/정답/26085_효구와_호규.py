from sys import stdin

def solution(columns, rows, grid):
    if (columns*rows)%2:
        return -1
    
    number_of_one = 0
    is_clearable = False
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(columns):
        for j in range(rows):
            if grid[i][j] == 1:
                number_of_one +=1
            for k in range(4):
                x = j + dx[k]
                y = i + dy[k]
                if 0<= x < rows and 0 <= y < columns:
                    if grid[i][j] == grid[y][x]:
                        is_clearable = True
    if is_clearable == True and not number_of_one % 2 :
        return 1
    return -1

columns, rows = map(int, stdin.readline().split(' '))
grid = list()
for _ in range(columns):
    grid.append(list(map(int, stdin.readline().split(' '))))

print(solution(columns, rows, grid))