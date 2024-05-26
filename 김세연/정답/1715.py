import sys
import heapq

input = sys.stdin.readline

N = int(input())

deck = [0] * N

for i in range(N):
    deck[i] = int(input())

heapq.heapify(deck)

if N == 1:
    print(0)
else:
    sum = 0
    while len(deck) > 1:
        a = heapq.heappop(deck)
        b = heapq.heappop(deck)
        p = a + b
        heapq.heappush(deck, p)
        sum += p
    
    print(sum)

