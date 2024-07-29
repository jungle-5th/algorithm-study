from sys import stdin
from collections import deque
input = stdin.readline

def pair_arange(pipe_a, pipe_b, value):
    if pipe_a < pipe_b: return pipe_a, pipe_b, value
    return pipe_b, pipe_a, value

def append_to_adj_list(pipe_a, pipe_b, adj_list):
    if pipe_a in adj_list.keys():
        adj_list[pipe_a].append(pipe_b)
    else:
        adj_list[pipe_a] = list()
        adj_list[pipe_a].append(pipe_b)
        
    if pipe_b in adj_list.keys():
        adj_list[pipe_b].append(pipe_a)
    else:
        adj_list[pipe_b] = list()
        adj_list[pipe_b].append(pipe_a)
        
def find_min_capacity_and_reduce(current_path, pipe_list):
    min_capacity = 10**9
    for i in range(len(current_path)-1):
        pipe_a, pipe_b, trash = pair_arange(current_path[i], current_path[i+1], "0")
        min_capacity = min(min_capacity, pipe_list[(pipe_a, pipe_b)])
    for i in range(len(current_path)-1):
        pipe_a, pipe_b, trash = pair_arange(current_path[i], current_path[i+1], "0")
        pipe_list[(pipe_a, pipe_b)] -= min_capacity
        
    return min_capacity

def max_flow(n_pipe):
    result = 0
    
    pipe_list = dict()
    adj_list = dict()
    for i in range(n_pipe):
        pipe_a, pipe_b, capacity = input().split(' ')
        pipe_a, pipe_b, capacity = pair_arange(pipe_a, pipe_b, capacity)
        if (pipe_a, pipe_b) in pipe_list.keys():
            pipe_list[(pipe_a, pipe_b)] += int(capacity)
        else:
            pipe_lisfrom sys import stdin
from collections import deque
input = stdin.readline

def pair_arange(pipe_a, pipe_b, value):
    if pipe_a < pipe_b: return pipe_a, pipe_b, value
    return pipe_b, pipe_a, value

def append_to_adj_list(pipe_a, pipe_b, adj_list):
    if pipe_a in adj_list.keys():
        adj_list[pipe_a].append(pipe_b)
    else:
        adj_list[pipe_a] = list()
        adj_list[pipe_a].append(pipe_b)
        
    if pipe_b in adj_list.keys():
        adj_list[pipe_b].append(pipe_a)
    else:
        adj_list[pipe_b] = list()
        adj_list[pipe_b].append(pipe_a)
        
def find_min_capacity_and_reduce(current_path, pipe_list):
    min_capacity = 10**9
    for i in range(len(current_path)-1):
        pipe_a, pipe_b, trash = pair_arange(current_path[i], current_path[i+1], "0")
        min_capacity = min(min_capacity, pipe_list[(pipe_a, pipe_b)])
    for i in range(len(current_path)-1):
        pipe_a, pipe_b, trash = pair_arange(current_path[i], current_path[i+1], "0")
        pipe_list[(pipe_a, pipe_b)] -= min_capacity
        
    return min_capacity

def max_flow(n_pipe):
    result = 0
    
    pipe_list = dict()
    adj_list = dict()
    for i in range(n_pipe):
        pipe_a, pipe_b, capacity = input().split(' ')
        pipe_a, pipe_b, capacity = pair_arange(pipe_a, pipe_b, capacity)
        if (pipe_a, pipe_b) in pipe_list.keys():
            pipe_list[(pipe_a, pipe_b)] += int(capacity)
        else:
            pipe_list[(pipe_a, pipe_b)] = int(capacity)
        append_to_adj_list(pipe_a, pipe_b, adj_list)
    
    while True:
        bfs = deque()
        bfs.append(['A'])
        visited = set()
        visited.add('A')
        path_found = False
        
        while bfs and not path_found:
            current_path = bfs.popleft()
            current_node = current_path[-1]
            for next_node in adj_list[current_node]:
                pipe_a, pipe_b, trash = pair_arange(current_node, next_node, "0")
                if next_node not in visited and pipe_list[(pipe_a, pipe_b)] > 0:
                    visited.add(next_node)
                    next_path = current_path.copy()
                    next_path.append(next_node)
                    if next_node == 'Z':
                        result += find_min_capacity_and_reduce(next_path, pipe_list)
                        path_found = True
                        break
                    bfs.append(next_path)
        
        if not path_found:
            break

    return result

n_pipe = int(input())
print(max_flow(n_pipe))
t[(pipe_a, pipe_b)] = int(capacity)
        append_to_adj_list(pipe_a, pipe_b, adj_list)
    
    visited_list = list()
    bfs = deque()
    bfs.append(['A'])
    while bfs:
        current_path = bfs.popleft()
        for next_node in adj_list[current_path[-1]]:
            if (current_path[-1], next_node) in visited_list: continue
            
            visited_list.append((current_path[-1], next_node))
            pipe_a, pipe_b, trash = pair_arange(current_path[-1], next_node, "0")
            if next_node == 'Z':
                next_path = current_path.copy()
                next_path.append(next_node)
                result += find_min_capacity_and_reduce(next_path, pipe_list)
            elif 0 < pipe_list[(pipe_a, pipe_b)]:
                next_path = current_path.copy()
                next_path.append(next_node)
                bfs.append(next_path)

    return result

n_pipe = int(input())

print(max_flow(n_pipe))