import sys

n_of_tanks, m_of_pipes, q_of_visits = map(int,input().split(" "))

water_q_input = list(map(int, sys.stdin.readline().split(" ")))
water_quality = [0] * (n_of_tanks+1)
for i in range(1, n_of_tanks+1):
    if water_q_input[i-1]: water_quality[i] = 1
    else: water_quality[i] = -1

pipes = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(m_of_pipes)]
# pipes = sorted(pipes)
flag = [i for i in range(n_of_tanks+1)]
sumres = [0] * (n_of_tanks + 1)

def find_union(cur):
    if flag[cur] == cur: return cur
    else:
        flag[cur] = find_union(flag[cur])
        return flag[cur]

for pipe in pipes:
    if find_union(pipe[0]) != find_union(pipe[1]):
        flag[find_union(pipe[1])] = flag[pipe[0]]

for tank in range(1,n_of_tanks+1):
    sumres[find_union(tank)] += water_quality[tank]

for _ in range(q_of_visits):
    tank = int(sys.stdin.readline())
    if sumres[find_union(tank)] > 0: print(1)
    else: print(0)