from sys import stdin
import copy
input = stdin.readline

def move_board(phase, map_size, board, count, value):
    if count == 5:
        return value
    max_value = value
    start_point = [(0, 0), (map_size-1, 0), (0, 0), (0, map_size-1)]
    
    move1 = [(1,0),(-1,0),(0,1),(0,-1)]
    move2 = [(0,1),(0,1),(1,0),(1,0)]
    
    y, x = start_point[phase]
    dy1, dx1 = move1[phase]
    dy2, dx2 = move2[phase]
    
    for i in range(map_size):
        for j in range(0, map_size-1):
            comb1_y, comb1_x = y + (dy1*j), x + (dx1*j)
            if board[comb1_y][comb1_x] == 0:
                continue
            for k in range(1, map_size-j):
                comb2_y, comb2_x = comb1_y + (dy1*k), comb1_x + (dx1*k)
                if board[comb1_y][comb1_x] == board[comb2_y][comb2_x]:
                    max_value = max(max_value, board[comb1_y][comb1_x]*2)
                    board[comb1_y][comb1_x] *= 2
                    board[comb2_y][comb2_x] = 0
                    break
                elif board[comb2_y][comb2_x] != 0:
                    break
        y, x = y + dy2, x + dx2

    y, x = start_point[phase]
    for i in range(map_size):
        comb_y, comb_x = y, x
        move = True
        while move:
            move = False
            for j in range(map_size - 1):
                if board[comb_y][comb_x] == 0 and board[comb_y+dy1][comb_x+dx1] != 0:
                    move = True
                    board[comb_y][comb_x] = board[comb_y+dy1][comb_x+dx1]
                    board[comb_y+dy1][comb_x+dx1] = 0
                comb_y, comb_x = comb_y + dy1, comb_x + dx1
            comb_y, comb_x = y, x
        y, x = y + dy2, x + dx2
    
    for i in range(4):
        temp = copy.deepcopy(board)
        max_value = max(max_value, move_board(i, map_size, temp, count+1, max_value))
        
    return max_value

def tzfe(map_size):
    board = list()
    max_value = 0
    for i in range(map_size):
        board.append(list(map(int, input().split(' '))))
    for line in board:
        max_value = max(max(line), max_value)
    for i in range(4):
        max_value = max(max_value, move_board(i, map_size, board, 0, max_value))
    
    return max_value

print(tzfe(int(input())))