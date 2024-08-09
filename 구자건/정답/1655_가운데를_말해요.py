from sys import stdin
from heapq import heappop, heappush
input = stdin.readline
def find_middle(small_list, big_list, new_number):
    if (not small_list)and(not big_list):
        print(new_number)
        heappush(small_list, -new_number)
        
    elif not big_list:
        number1 = -heappop(small_list)
        number1, new_number = min(number1, new_number), max(number1, new_number)
        print(number1)
        heappush(small_list, -number1)
        heappush(big_list, new_number)
    
    else:
        if big_list[0] <= new_number:
            heappush(big_list, new_number)
        else:
            heappush(small_list, -new_number)
        
        if len(small_list) < len(big_list):
            while len(small_list) < len(big_list):
                heappush(small_list, -heappop(big_list))
        elif len(small_list) > len(big_list)+1:
            while len(small_list) > len(big_list)+1:
                heappush(big_list, -heappop(small_list))
        print(-small_list[0])
    return

def tell_middle(n_number):
    small_list = list()
    big_list = list()
    
    for i in range(n_number):
        new_number = int(input())
        find_middle(small_list, big_list, new_number)

n_number = int(input())
tell_middle(n_number)