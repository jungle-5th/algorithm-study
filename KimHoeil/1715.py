# 카드정렬하기
# 1715번

import sys
import heapq
input = sys.stdin.readline

n = int(input())

minq = []
for i in range(n):
     num = int(input())
     heapq.heappush(minq, num)

sum = 0
while len(minq)  > 1:
     a = heapq.heappop(minq)
     b = heapq.heappop(minq)
     temp = a+b
     sum += temp
     heapq.heappush(minq, temp)

print(sum)
