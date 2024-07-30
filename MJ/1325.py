# https://www.acmicpc.net/problem/1325
# 효율적인 해킹

# 문제
# 해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다.
# 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.
# 이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데,
# A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.
# 이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다.
# 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다.
# 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

# 출력
# 첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

# 예제 입력 1 
# 5 4
# 3 1
# 3 2
# 4 3
# 5 3
# 예제 출력 1 
# 1 2

import sys
from collections import deque

n_of_pc, m_of_link = map(int, sys.stdin.readline().split(" "))
candidate = [0] *(n_of_pc+1)
adjlist = [[] for _ in range(n_of_pc+1)]
for _ in range(m_of_link):
    to, frm = map(int, sys.stdin.readline().split(" "))
    candidate[frm] = 1
    adjlist[frm].append(to)

max = 0
res = []

for i in range(n_of_pc+1):
    # candidate>0인 후보들 BFS하면서 카운트 셈
    if candidate[i]==0: continue
    visited = [False] *(n_of_pc+1)
    q = deque()
    q.append(i)
    visited[i] = True
    while len(q) != 0:
        cur = q.popleft()
        for j in range(len(adjlist[cur])):
            check = adjlist[cur][j]
            if not visited[check]:
                q.append(check)
                visited[check] = True
                candidate[i] += 1

    if candidate[i] > max:
        max = candidate[i]
        res.clear()
        res.append(i)
    elif candidate[i] == max:
        res.append(i)

while res: print(res.pop(0), end=" ")