from sys import stdin
from collections import deque
input = stdin.readline

def exchange(number, count):
    visited_map = [set() for j in range(2)]
    n_number = 0
    test_number = number
    while test_number:
        n_number += 1
        test_number //= 10
    
    bfs = deque()
    bfs.append([number, 0])
    max_value = -1
    while bfs:
        cur_number, cur_count = bfs.popleft()
        if count <= cur_count:
            break
        
        for i in range(n_number-1):
            for j in range(i+1, n_number):
                first_number = ((cur_number - ((cur_number//10**(i+1))*(10**(i+1)))) - cur_number % 10**(i))//10**(i)
                second_number = ((cur_number - ((cur_number//10**(j+1))*(10**(j+1)))) - cur_number % 10**(j))//10**(j)
                
                new_number = cur_number - (first_number*(10**(i))) + (second_number*(10**(i))) - (second_number*(10**(j))) + (first_number*(10**(j)))
                if new_number < 10**(n_number - 1):
                    continue
                elif new_number in visited_map[(cur_count+1)%2]:
                    continue
                if (count - cur_count)%2:
                    max_value = max(max_value, new_number)
                visited_map[(cur_count+1)%2].add(new_number)
                bfs.append([new_number, cur_count+1])
    return max_value
number, count = map(int, input().split(' '))
print(exchange(number, count))