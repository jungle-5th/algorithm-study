from sys import stdin
input = stdin.readline

def find_root(kingdom_list, cur_node):
    if kingdom_list[cur_node] < 0:
        return cur_node
    kingdom_list[cur_node] =  find_root(kingdom_list, kingdom_list[cur_node])
    return kingdom_list[cur_node]

def union_mating():
    n_kingdom, n_union = map(int, input().split(' '))
    kingdom_list = [-1 for _ in range(n_kingdom + 1)]
    for i in range(n_union):
        kingdom_a, kingdom_b = map(int, input().split(' '))
        root_a = find_root(kingdom_list, kingdom_a)
        root_b = find_root(kingdom_list, kingdom_b)
        if root_a != root_b:
            if root_a < root_b:
                kingdom_list[root_a] += kingdom_list[root_b]
                kingdom_list[root_b] = root_a
            else:
                kingdom_list[root_b] += kingdom_list[root_a]
                kingdom_list[root_a] = root_b
    
    c_kingdom, h_kingdom, opportunity = map(int, input().split(' '))
    c_root = find_root(kingdom_list, c_kingdom)
    h_root = find_root(kingdom_list, h_kingdom)
    
    neutral_union = list()
    
    for kingdom in range(1, n_kingdom):
        if kingdom_list[kingdom] < 0 and kingdom != c_root and kingdom != h_root:
            neutral_union.append(kingdom_list[kingdom])
    
    neutral_union.sort()
    n_merge = min(opportunity, len(neutral_union))

    for i in range(n_merge):
        kingdom_list[c_root] += neutral_union[i]
    
    return -kingdom_list[c_root]

print(union_mating())