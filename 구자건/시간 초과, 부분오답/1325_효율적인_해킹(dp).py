from sys import stdin
from collections import deque

input = stdin.readline

def bfs_and_add_count(target_pc, adj_list, n_hack_count):
    bfs = deque()
    bfs.append(target_pc)
    count = 0
    while bfs:
        cur_pc = bfs.popleft()
        for next_pc in adj_list[cur_pc]:
            if target_pc != next_pc and len(n_hack_count[next_pc]) == 0:
                n_hack_count[target_pc].add(next_pc)
                bfs.append(next_pc)
            else: n_hack_count[target_pc] = n_hack_count[target_pc].union(n_hack_count[next_pc])
    return

def efficient_hack(n_pc, n_trust):
    adj_list = [list() for _ in range(n_pc+1)]
    n_hack_count = [set() for _ in range(n_pc+1)]
    for i in range(n_trust):
        trusting_pc, trusted_pc = map(int, input().split(' '))
        adj_list[trusted_pc].append(trusting_pc)
    
    max_count = 0
    for i in range(1, n_pc+1):
        bfs_and_add_count(i, adj_list, n_hack_count)
        max_count = max(max_count, len(n_hack_count[i]))
    
    output_list = list()
    for i in range(1, n_pc+1):
        if len(n_hack_count[i]) == max_count:
            output_list.append(i)
    print(*output_list)
    
    return

n_pc, n_trust = map(int, input().split(' '))
k = set()
efficient_hack(n_pc, n_trust)