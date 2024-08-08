from sys import stdin
from collections import deque
input = stdin.readline

def snake(map_size):
    phase = [[0, 1],[1, 0],[0, -1],[-1, 0]]
    snake = deque()
    apple_map = [[False for i in range(map_size)]for i in range(map_size)]
    
    n_apple = int(input())
    for apple in range(n_apple):
        apple_column, apple_row = map(int, input().split(' '))
        apple_map[apple_column-1][apple_row-1] = True
    
    n_command = int(input())
    command_list = deque()
    for commend in range(n_command):
        commend_time, commend_key = input().rstrip().split(' ')
        command_list.append([int(commend_time), commend_key])
    
    
    snake.append([0, 0])
    cur_column = 0
    cur_row = 0
    
    cur_phase = 0
    time = 0
    while True:
        time += 1
        
        dy, dx = phase[cur_phase%4]
        cur_column += dy
        cur_row += dx
        
        if (not 0 <= cur_column < map_size) or  (not 0 <= cur_row < map_size) or ([cur_column, cur_row] in snake):
            break
        
        snake.append([cur_column, cur_row])
        
        if command_list and time == command_list[0][0]:
                _, commend_key = command_list.popleft()
                if commend_key == "L": cur_phase -= 1
                else: cur_phase += 1
        
        if apple_map[cur_column][cur_row] == True:
            apple_map[cur_column][cur_row] = False
            continue
        
        snake.popleft()
    
    return time

map_size = int(input())
print(snake(map_size))