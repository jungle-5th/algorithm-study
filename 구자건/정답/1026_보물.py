from sys import stdin
from heapq import heappop, heappush
def treasure(A_list,B_list):
    sum = 0
    heap_a = list()
    heap_b = list()
    for a in A_list:
        heappush(heap_a, a)
    for b in B_list:
        heappush(heap_b, -b)
    while heap_a:
        a = heappop(heap_a)
        b = -heappop(heap_b)
        sum += a*b
    return sum

numbers = int(stdin.readline())
A_list = list(map(int, stdin.readline().split(' ')))
B_list = list(map(int, stdin.readline().split(' ')))

print(treasure(A_list, B_list))