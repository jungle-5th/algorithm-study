from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

def hide_and_seek(sister_start, brother_hide):
    if sister_start == brother_hide : return 0
    visited_list = [False for _ in range(100001)]
    bfs = list()
    heappush(bfs, [0,sister_start])
    visited_list[sister_start] = True
    
    while(bfs):
        cur_move, cur_sister = heappop(bfs)
        
        if 0 <= 2*cur_sister <= 100000 and visited_list[2*cur_sister] == False:
            if 2*cur_sister == brother_hide:
                return cur_move
            heappush(bfs, [cur_move, 2*cur_sister])
            visited_list[2*cur_sister] = True
            
        if 0 <= cur_sister+1 <= 100000 and visited_list[cur_sister+1] == False:
            if cur_sister+1 == brother_hide:
                return cur_move+1
            heappush(bfs, [cur_move+1, cur_sister+1])
            visited_list[cur_sister+1] = True
            
        if 0 <= cur_sister-1 <= 100000 and visited_list[cur_sister-1] == False:
            if cur_sister-1 == brother_hide:
                return cur_move+1
            heappush(bfs, [cur_move+1, cur_sister-1])
            visited_list[cur_sister-1] = True
    return -1

sister, brother = map(int, input().split(' '))

print(hide_and_seek(sister, brother))