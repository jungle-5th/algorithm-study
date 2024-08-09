from sys import stdin
input = stdin.readline
#     북
# 서      동
#     남

def dice_rolling(map_row, map_column, dice_row, dice_column, n_order):
    dice = [ 0 for i in range(6)]
    dice_map = [[4, 3, 5, 2],[4, 3, 1, 6],[],[],[],[]]
    
    board_map = list()
    for i in range(map_row):
        board_map.append(list(map(int, input().split(' '))))
    order_list = list(map(int, input().split(' ')))
    
    cur_board_column, cur_board_row = dice_row, dice_column
    cur_dice_row, cur_dice_column = 0, 0
    
    for order in range(n_order):
        
        board_dy = [0, 0, -1, 1]
        board_dx = [1, -1, 0, 0]
        
        order_index = order_list[order]-1
        
        if not(0 <= cur_board_column + board_dy[order_index] < map_row) or not(0 <= cur_board_row + board_dx[order_index] < map_column):
            continue
        
        cur_board_column, cur_board_row = cur_board_column + board_dy[order_index], cur_board_row + board_dx[order_index]
        
        cur_dice_column, cur_dice_row = cur_dice_column + dice_dy[order_index], cur_dice_row + dice_dx[order_index]
        
        if board_map[cur_board_column][cur_board_row] == 0:
            board_map[cur_board_column][cur_board_row] = dice[dice_map[cur_dice_column-2%4][cur_board_row-2%4]-1]
        else:
            dice[dice_map[(cur_dice_column+2)%4][(cur_board_row)%4]-1] = board_map[cur_board_column][cur_board_row]
            board_map[cur_board_column][cur_board_row] = 0
        print (dice[dice_map[cur_dice_column%4][cur_board_row%4]-1])
        
    return

map_row, map_column, dice_row, dice_column, n_order = map(int, input().split(' '))
dice_rolling(map_row, map_column, dice_row, dice_column, n_order)