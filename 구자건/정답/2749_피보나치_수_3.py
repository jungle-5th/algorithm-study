from sys import stdin
from collections import deque
def fivo(n_number):
    if n_number == 1:
        return 1
    if n_number == 2:
        return 1
    
    fivo_list = deque()
    fivo_list.append(1)
    fivo_list.append(1)
    n = 2
    while n != n_number :
        result = (fivo_list[n-1] + fivo_list[n-2]) % 1000000
        if result == 1 and fivo_list[n-1] == 1:
            fivo_list.pop()
            return fivo_list[ n_number % len(fivo_list) -1 ]
        fivo_list.append(result)
        n += 1
    
    return fivo_list[-1]

print(fivo(int(input())))