from sys import stdin
from collections import deque
input = stdin.readline

def ho_ban_woo(n_cow):
    cow_list = list(map(int, input().split(' ')))
    cow_list.sort()
    cow_list = deque(cow_list)

    count = 0
    length = len(cow_list)
    for i in range(length):
        index = (i + length)//2
        count += cow_list[index]

    return count

n_cow = int(input())

print(ho_ban_woo(n_cow))