import sys
import heapq
input = sys.stdin.readline

n = int(input())
cards = []
sum=0
for _ in range(n):
    heapq.heappush(cards, int(input()))
while cards:
    try:
        output1 = heapq.heappop(cards)
        output2 = heapq.heappop(cards)
        if(output2):
            sum+=output1+output2
            heapq.heappush(cards, output1+output2)
    except:
        break
print(sum)