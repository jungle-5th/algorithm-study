from collections import deque
def hide_and_seek(sister, brother):
    if sister == brother:
        return 0
    
    cur_brother = brother
    bfs = deque()
    table[sister] = True
    bfs.append((0, sister, brother))
    
    while cur_brother < 500001:
        cur = bfs.popleft()
        time = cur[0]
        cur_sister = cur[1]
        cur_brother = cur[2]
        if table[cur_brother] == True:
            return time
        
        if 0<= cur_sister - 1:
            if table[cur_sister - 1] == False:
                table[cur_sister - 1] = True
                bfs.append((time+1, cur_sister - 1, cur_brother+time+1))

        if cur_sister + 1 < 500001:
            if table[cur_sister + 1] == False:
                table[cur_sister + 1] = True
                bfs.append((time+1, cur_sister + 1, cur_brother+time+1))

        if cur_sister * 2 < 500001:
            if table[cur_sister * 2] == False:
                table[cur_sister * 2] = True
                bfs.append((time+1, cur_sister * 2, cur_brother+time+1))
        if 500000 < cur_brother+time+1:
            break
    return -1
table = [False for _ in range(500001)]

sister, brother = map(int, input().split(' '))
print(hide_and_seek(sister, brother))