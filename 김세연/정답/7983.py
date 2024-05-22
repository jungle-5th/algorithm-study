# 백준 7983: 내일 할 거야

from heapq import heappush, heappop

import sys

input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    d, t = map(int, input().split())
    heappush(heap, (-t, d))

# 첫 원소 꺼내서 시작하기
start, work = heappop(heap)
start = start * (-1) - work

# 우선순위 큐에 원소가 있는 경우 계속 찾기
while heap:
    x, work = heappop(heap)
    x *= -1
    start = min(start, x) - work

print(start)
