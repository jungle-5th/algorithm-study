from sys import stdin
from collections import deque
input = stdin.readline


n_kingdom, n_union = map(int, input().split(' '))
adj_list = [list() for _ in range(n_kingdom + 1)]
visited_list = [False for _ in range(n_kingdom + 1)]

for _ in range(n_union):
    kingdom_a, kingdom_b = map(int, input().split(' '))
    adj_list[kingdom_a].append(kingdom_b)
    adj_list[kingdom_b].append(kingdom_a)

c_kingdom, h_kingdom, opportunity = map(int, input().split(' '))

bfs = deque()
c_union = 1
bfs.append(c_kingdom)
visited_list[c_kingdom] = True
while bfs:
    cur_kingdom = bfs.popleft()
    
    for union in adj_list[cur_kingdom]:
        if visited_list[union] == False:
            c_union += 1
            visited_list[union] = True
            bfs.append(union)
bfs.append(h_kingdom)
visited_list[h_kingdom] = True
while bfs:
    cur_kingdom = bfs.popleft()
    
    for union in adj_list[cur_kingdom]:
        if visited_list[union] == False:
            visited_list[union] = True
            bfs.append(union)
union_list = list()
for i in range(n_kingdom+1):
    if visited_list[i] == False:
        size = len(union_list)
        union_list.append(1)
        bfs.append(i)
        visited_list[i] = True
        
        while bfs:
            cur_kingdom = bfs.popleft()
            for union in adj_list[cur_kingdom]:
                if visited_list[union] == False:
                    visited_list[union] = True
                    bfs.append(union)
                    union_list[size-1] += 1

union_list.sort(reverse=True)
min_value = min(opportunity, len(union_list))
for i in range(min_value):
    c_union += union_list[i]

print(c_union)