from sys import stdin
from collections import deque

input  = stdin.readline

def hide_and_seek(sister_start, brother_start):
    if sister_start == brother_start:
        return 0
    
    valid_point = [True for _ in range(500001)]
    bfs = deque()
    
    cur_brother = brother_start
    checked_brother = brother_start
    bfs.append([sister_start, brother_start, 1])
    while(bfs):
        if 500000 < cur_brother + cur_speed:
            return -1

        cur_sister, cur_brother, cur_speed = bfs.popleft()
        if checked_brother != cur_brother:
            is_valid_point(valid_point, cur_brother, cur_speed)
            checked_brother = cur_brother
        
        if 0 <= 2*cur_sister <= 500000 and valid_point[2*cur_sister] == True:
            if 2*cur_sister == cur_brother + cur_speed:
                return cur_speed
            bfs.append([2*cur_sister, cur_brother + cur_speed, cur_speed+1])
            
        if 0 <= 2*cur_sister <= 500000 and valid_point[2*cur_sister] == True:
            if cur_sister+1 == cur_brother + cur_speed:
                return cur_speed
            bfs.append([cur_sister+1, cur_brother + cur_speed, cur_speed+1])
            
        if 0 <= cur_sister-1 <= 500000 and valid_point[2*cur_sister] == True:
            if cur_sister-1 == cur_brother + cur_speed:
                return cur_speed
            bfs.append([cur_sister-1, cur_brother + cur_speed, cur_speed+1])
    
    return -1

def is_valid_point(valid_point, cur_brother, cur_speed):
    count = 0
    brother = cur_brother
    speed = cur_speed
    while cur_brother + speed < 500001:
        count += 1
        speed += 1

    

sister, brother = map(int, input().split(' '))

print(hide_and_seek(sister, brother))