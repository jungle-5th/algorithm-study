from sys import stdin
from collections import deque
from heapq import heappop, heappush
n_node = int(stdin.readline())
parent_list = [[0, 0] for _ in range(n_node + 1)]
child_list = [list() for _ in range(n_node + 1)]
layer_map = dict()
depth = [0 for _ in range(n_node + 1)]
max_diameter = 0

for node in range(2, n_node+1):
    parent, cur, weight = map(int, stdin.readline().split(' '))
    parent_list[cur] = [parent, weight]
    child_list[parent].append([cur, weight])

root = 1
while root != 0:
    if parent_list[root][0] == 0:
        break
    root = parent_list[root]
    
layer_table = list()
layer_table.append(list())
layer_table.append(list())
layer_table[0].append(root)

bfs = deque()
bfs.append([root, 0])
depth[root] = 0
while bfs:
    cur_node, cur_layer = bfs.popleft()
    if cur_layer >= len(layer_table)-1:
        layer_table.append(list())

    for child, child_weight in child_list[cur_node]:
        layer_table[cur_layer+1].append(child)
        depth[child] = depth[cur_node] + child_weight
        bfs.append([child, cur_layer+1])

tree_size = len(layer_table)
sub_tree = [list() for _ in range(n_node + 1)]

for i in range(0, tree_size):
    cur_layer = tree_size - i -1
    for node in layer_table[cur_layer]:
        if len(sub_tree[node]) == 0:
            biggest_sub_tree = 0
            second_biggest_sub_tree = 0
        elif len(sub_tree[node]) == 1:
            biggest_sub_tree = -heappop(sub_tree[node])
            second_biggest_sub_tree = 0
        else :
            biggest_sub_tree = -heappop(sub_tree[node])
            second_biggest_sub_tree = -heappop(sub_tree[node])
        
        cur_diameter = biggest_sub_tree + max(depth[node], second_biggest_sub_tree)
        max_diameter = max(cur_diameter, max_diameter)
        
        parent, weight = parent_list[node][0], parent_list[node][1]
        
        heappush(sub_tree[parent], -(biggest_sub_tree + weight))
print(max_diameter)