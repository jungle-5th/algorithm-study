from sys import stdin
import copy
input = stdin.readline
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

def shark():
    fish_list = [list() for i in range(17)]
    ocean_map = [[0 for i in range(4)]for j in range(4)]
    for i in range(4):
        input_line = list(map(int, input().split(' ')))
        for j in range(4):
            fish_number = input_line[j*2]
            fish_direction = input_line[j*2+1]
            fish_list[fish_number] = [i, j, fish_direction-1]
            ocean_map[i][j] = fish_number
            
    dead_number = ocean_map[0][0]
    trash1, trash2, direction = fish_list[dead_number]
    fish_list[dead_number] = [-1, -1, -1]
    ocean_map[0][0] = -1
    fish_list[0] = [0, 0 ,direction]
    
    return move(fish_list, ocean_map, dead_number)

def fish_move(fish_list, ocean_map):
    for fish in range(1, 17):
        column, row, direction = fish_list[fish]
        if direction == -1:
            continue
        
        for i in range(8):
            dy, dx = directions[direction]
            next_column, next_row = column + dy, row + dx

            if 0 <= next_row < 4 and 0 <= next_column < 4 and ocean_map[next_column][next_row] != -1:
                if 0 < ocean_map[next_column][next_row]:
                    changed_fish_number = ocean_map[next_column][next_row]
                    changed_fish_column, changed_fish_row, changed_fish_direction = fish_list[changed_fish_number]
                    
                    fish_list[changed_fish_number] = [column, row, changed_fish_direction]
                    ocean_map[column][row] = changed_fish_number
                else:
                    ocean_map[column][row] = 0
                fish_list[fish] = [next_column, next_row, direction]
                ocean_map[next_column][next_row] = fish
                break

            else:
                direction = (direction + 1) % 8
    return


def move(fish_list, ocean_map, count):
    max_count = count
    
    fish_move(fish_list, ocean_map)
    before_shark_column, before_shark_row, shark_direction = fish_list[0]
    dy, dx = directions[shark_direction]
    
    temp_list = copy.deepcopy(fish_list)
    temp_map = copy.deepcopy(ocean_map)
    
    shark_column = before_shark_column + dy
    shark_row = before_shark_row + dx
    while 0 <= shark_column < 4 and 0 <= shark_row < 4 :
        if 0 < ocean_map[shark_column][shark_row]:
            dead_fish = ocean_map[shark_column][shark_row]
            trash, trash, direction = fish_list[dead_fish]
            
            fish_list[dead_fish] = [-1, -1, -1]
            fish_list[0] = [shark_column, shark_row, direction]
            
            ocean_map[shark_column][shark_row] = -1
            ocean_map[before_shark_column][before_shark_row] = 0
            max_count = max(max_count, move(fish_list, ocean_map, count+dead_fish))
            fish_list = copy.deepcopy(temp_list)
            ocean_map = copy.deepcopy(temp_map)
        shark_column += dy
        shark_row += dx
    return max_count

print(shark())