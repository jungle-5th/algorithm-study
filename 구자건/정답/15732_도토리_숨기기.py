from sys import stdin
from heapq import heappop, heappush

def hide_acorns():
    lp = min_box
    rp = max_box
    search_point = (lp + rp)//2
    
    answer_list = list()
    
    min_search = 10**9
    while lp<=rp:
        searched_acorn = 0
        search_point = (lp + rp)//2
        for pattern in patterns:
            boxes = ((min(search_point, pattern[1]) - pattern[0]) // pattern[2])+1
            if 0 < boxes:
                searched_acorn += boxes
        
        if searched_acorn < n_acorn:
            lp = search_point+1
        else:
            min_search = min(min_search, search_point)
            rp = search_point-1
    return min_search


n_box, n_pattern, n_acorn = map(int, stdin.readline().split(' '))
patterns = list()
min_box = 10**9
max_box = 0
for _ in range(n_pattern):
    pattern = list(map(int, stdin.readline().split(' ')))
    patterns.append(pattern)
    min_box = min(min_box, pattern[0])
    max_box = max(max_box, pattern[1])
print(hide_acorns())