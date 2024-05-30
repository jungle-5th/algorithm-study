from sys import stdin
from collections import deque
input = stdin.readline

def racoon_99():
    max_weight = 0
    visited_list[0] = 0
    
    bfs_que.append([0,0])
    while bfs_que:
        cur_room, cur_weight = bfs_que.popleft()
        for room, weight in adj_list[cur_room]:
            if visited_list[room] == False:
                visited_list[room] = True
                bfs_que.append([room, cur_weight+weight])
                max_weight = max(max_weight, cur_weight+weight)
    return max_weight

n_room = int(input())
bfs_que = deque()
adj_list = [list() for i in range(n_room)]
visited_list = [False for i in range(n_room)]

for i in range(n_room-1):
    a, b, weight = map(int, input().split())
    adj_list[a-1].append([b-1, weight])
    adj_list[b-1].append([a-1, weight])

print(racoon_99())