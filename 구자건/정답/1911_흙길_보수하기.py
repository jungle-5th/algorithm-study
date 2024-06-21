from sys import stdin
from heapq import heapify, heappop, heappush
input = stdin.readline

def repair_road(port_hole_list, board_size):
    count = 0
    before_coordinate = 2*(10**9)
    while port_hole_list:
        start, end = port_hole_list.pop(0)
        
        if before_coordinate < end:
            end = before_coordinate
        
        board_count = ((end - start)//board_size)
        if (end - start)%board_size != 0:
            board_count += 1
        count += board_count
        
        before_coordinate = end - board_count*board_size
    return count

n_port_hole, board_size = map(int, input().split(' '))
port_hole_list = list()
for _ in range(n_port_hole):
    start, end = map(int, input().split(' '))
    port_hole_list.append([start, end])
port_hole_list.sort(reverse=True)


print(repair_road(port_hole_list, board_size))