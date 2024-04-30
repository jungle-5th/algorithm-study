from sys import stdin
from heapq import heappush, heappop
def spacial_reword(seats):
    find_second_list = list()
    
    if len(seats[0]) ==1:
        return seats[0][0]

    edge = len(seats[0])//2
    cur_column = len(seats[0])
    heappush(find_second_list, spacial_reword([[seats[i][j] for i in range(edge)] for j in range(edge)]))
    heappush(find_second_list, spacial_reword([[seats[i][j] for i in range(edge, cur_column)] for j in range(edge)]))
    heappush(find_second_list, spacial_reword([[seats[i][j] for i in range(edge)] for j in range(edge, cur_column)]))
    heappush(find_second_list, spacial_reword([[seats[i][j] for i in range(edge, cur_column)] for j in range(edge, cur_column)]))
    heappop(find_second_list)
    return heappop(find_second_list)

column = int(stdin.readline())
seats = list()
for _ in range(column):
    seats.append(list(map(int, stdin.readline().split(' '))))

print(spacial_reword(seats))