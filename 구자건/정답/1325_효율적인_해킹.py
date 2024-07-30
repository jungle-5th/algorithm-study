from sys import stdin
from collections import deque

input = stdin.readline

def bfs_and_add_count(target_pc, adj_list, n_pc):
    visited_list = [False for i in range(n_pc+1)]
    bfs = deque()
    bfs.append(target_pc)
    visited_list[target_pc] = True
    count = 0
    while bfs:
        cur_pc = bfs.popleft()
        for next_pc in adj_list[cur_pc]:
            if visited_list[next_pc] == False:
                count += 1
                visited_list[next_pc] = True
                bfs.append(next_pc)
    return count

def efficient_hack(n_pc, n_trust):
    adj_list = [list() for _ in range(n_pc+1)]
    n_hack_count = [0 for _ in range(n_pc+1)]
    for i in range(n_trust):
        trusting_pc, trusted_pc = map(int, input().split(' '))
        adj_list[trusted_pc].append(trusting_pc)
    
    for i in range(1, n_pc+1):
        n_hack_count[i] = bfs_and_add_count(i, adj_list, n_pc)
    
    max_count = max(n_hack_count)
    
    output_list = list()
    for i in range(1, n_pc+1):
        if n_hack_count[i] == max_count:
            output_list.append(i)
    
    print(*output_list)
    return

n_pc, n_trust = map(int, input().split(' '))

efficient_hack(n_pc, n_trust)