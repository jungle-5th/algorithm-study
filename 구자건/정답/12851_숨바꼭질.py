from sys import stdin
from collections import deque
input = stdin.readline

def hide_and_seek(sister, brother):
    visited_list = [[10**9,0] for _ in range(100001)]
    bfs_que = deque()
    
    bfs_que.append([sister, 0])
    visited_list[sister][0] = 0
    visited_list[sister][1] = 1
    while(bfs_que):
        cur_sister, cur_time = bfs_que.popleft()
        if cur_time >= visited_list[brother][0]:
            break
        
        if cur_sister + 1 < 100001:
            if cur_time + 1 <= visited_list[cur_sister + 1][0]:
                if cur_time + 1 < visited_list[cur_sister + 1][0]:
                    bfs_que.append([cur_sister + 1, cur_time + 1])
                visited_list[cur_sister + 1][0] = cur_time + 1
                visited_list[cur_sister + 1][1] += visited_list[cur_sister][1]
                
        if 0 <= cur_sister -1:
            if cur_time + 1 <= visited_list[cur_sister - 1][0]:
                if cur_time + 1 < visited_list[cur_sister - 1][0]:
                    bfs_que.append([cur_sister - 1, cur_time + 1])
                visited_list[cur_sister - 1][0] = cur_time + 1
                visited_list[cur_sister - 1][1] += visited_list[cur_sister][1]
                
        if cur_sister*2 < 100001:
            if cur_time + 1 <= visited_list[cur_sister*2][0]:
                if cur_time + 1 < visited_list[cur_sister * 2][0]:
                    bfs_que.append([cur_sister * 2, cur_time + 1])
                visited_list[cur_sister*2][0] = cur_time + 1
                visited_list[cur_sister*2][1] += visited_list[cur_sister][1]

    print(visited_list[brother][0])
    print(visited_list[brother][1])
    return

sister, brother = map(int, input().split(' '))
hide_and_seek(sister, brother)