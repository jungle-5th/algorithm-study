from sys import stdin
from collections import deque

input = stdin.readline

def exit(number, n_try, target_number):
    if number == target_number:
        print(0)
        return
    bfs = deque()
    bfs.append([number, 0])
    visited_list = [False for i in range(100000)]
    while bfs:
        cur_number, cur_try = bfs.popleft()
        if n_try <= cur_try:
            print('ANG')
            return
        if cur_number+1 < 100000 and visited_list[cur_number+1] == False:
            if cur_number+1 == target_number:
                print(cur_try+1)
                return
            visited_list[cur_number+1] = True
            bfs.append([cur_number+1, cur_try+1])
        if cur_number*2 < 100000:
            next_number = cur_number*2
            if next_number//10000:
                next_number-=10000
            elif next_number//1000:
                next_number-=1000
            elif next_number//100:
                next_number-=100
            elif next_number//10:
                next_number-=10
            else : next_number-=1
            if 0<next_number<100000 and visited_list[next_number] == False:
                if next_number == target_number:
                    print(cur_try+1)
                    return
                visited_list[next_number] = True
                bfs.append([next_number, cur_try+1])
    print('ANG')
    return

number, n_try, target_number = map(int, input().split(' '))
exit(number, n_try, target_number)