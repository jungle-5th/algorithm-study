from sys import stdin

def sky_line(buildings, n_building):
    lp = 0
    rp = n_building-1
    while(lp < n_building):
        seek_pointer = lp - 1
        cur_top_height = buildings[lp]
        while(0 <= seek_pointer):
            if cur_top_height < buildings[seek_pointer]:
                dp_table[lp][0] = dp_table[seek_pointer][0] + 1
                first_view[lp][0] = seek_pointer
                break
            seek_pointer -= 1
        lp += 1
        
    while(0 <= rp):
        seek_pointer = rp + 1
        cur_top_height = buildings[rp]
        while(seek_pointer < n_building):
            if cur_top_height < buildings[seek_pointer]:
                dp_table[rp][1] = dp_table[seek_pointer][1] + 1
                first_view[rp][1] = seek_pointer
                break
            seek_pointer += 1
        rp -= 1
        
n_building = int(stdin.readline())
buildings = buildings = list(map(int, stdin.readline().split(' ')))
dp_table =[[0,0] for _ in range(n_building)]
first_view = [[-10**9, 10**9] for _ in range(n_building)]

sky_line(buildings, n_building)

for i in range(n_building):
    if dp_table[i][0] + dp_table[i][1] == 0:
        print(0)
        continue
    print(f'{dp_table[i][0] + dp_table[i][1]}', end=' ')
    if i - first_view[i][0] > first_view[i][1] - i :
        print(first_view[i][1] + 1)
    else: print(first_view[i][0] + 1)