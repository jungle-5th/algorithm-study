from sys import stdin
from collections import deque

def moving_night(board_size, checker_board, knight, target):
    dx = [-1, 1, -1, 1, 2, 2, -2, -2]
    dy = [2, 2, -2, -2, -1, 1, -1, 1]
    move_count = 0
    current_position = knight
    positions = deque()
    
    if current_position == target:
        return move_count
    
    positions.append((current_position, move_count))
    checker_board[current_position[0]][current_position[1]] = True
    
    while True:
        current_position, move_count = positions.popleft()
        for i in range(8):
            y = current_position[0] + dy[i]
            x = current_position[1] + dx[i]
            if(0 <= x <board_size and 0 <= y <board_size):
                if checker_board[y][x] == True:
                    continue
                if (y,x) == target:
                    return move_count+1
                positions.append(((y,x), move_count+1))
                checker_board[y][x] = True

test_case = int(stdin.readline())
for test in range(test_case):
    board_size = int(stdin.readline()) 
    knightX, knightY = map(int, stdin.readline().split(' '))
    targetX, targetY = map(int, stdin.readline().split(' '))
    checker_board = [[False for _ in range(board_size)]for __ in range(board_size)]
    print(moving_night(board_size, checker_board, (knightY, knightX), (targetY, targetX)))