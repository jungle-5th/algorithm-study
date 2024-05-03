from sys import stdin
def union_find():
    for tank in range(n_tank + 1):
        if tank < union[tank]:
            union[tank] = tank
        
        for adj in tanks[tank]:
            union[adj] = union[tank]
    
    for tank in range(1, n_tank + 1):
        if tank_list[tank] == 1:
            pure_list[union[tank]] += 1
        else: pure_list[union[tank]] -= 1
    return

n_tank, n_pipes, n_visit = map(int, stdin.readline().split(' '))
tank_list = [0]+list(map(int, stdin.readline().split(' ')))
tanks = [list() for _ in range(n_tank+1)]
union = [10**9 for _ in range(n_tank+1)]
pure_list = [0 for _ in range(n_tank+1)]

for _ in range(n_pipes):
    a, b = map(int, stdin.readline().split(' '))
    if a != b:
        if not a in tanks[b]:
            tanks[b].append(a)
        if not b in tanks[a]:
            tanks[a].append(b)

union_find()

for visit in range(n_visit):
    visited_tank = int(stdin.readline())
    if 0 < pure_list[union[visited_tank]]:
        print(1)
    else:
        print(0)