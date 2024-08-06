# https://www.acmicpc.net/problem/19236
# 청소년 상어
import copy

directions = [[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1]]
res = 0

# 물고기 이동
def fishmove(map):
    for fishnum in range(1,17):
        # fishnum에 해당하는 물고기 좌표 찾기
        found = False
        for y in range(4):
            if found: break
            for x in range(4):
                if found: break
                if map[y][x][0] != fishnum: continue
                fishdirIdx = map[y][x][1]%8
                while True: # 벽이거나 상어인 경우 방향을 틀어주면서 물고기 위치 이동
                    newy = y + directions[fishdirIdx][0]
                    newx = x + directions[fishdirIdx][1]
                    if newy < 0 or newy > 3 or newx < 0 or newx > 3 or map[newy][newx][0] == -1:
                        fishdirIdx = (fishdirIdx+1)%8
                        continue
                    map[y][x] = map[newy][newx]
                    map[newy][newx] = [fishnum, fishdirIdx]
                    found = True # 위치 이동한 물고기를 다시 찾지 않도록 하는 플래그
                    break
    return map

def sharking(map, cord, sum):
    global res
    sum += map[cord[0]][cord[1]][0]
    if sum > res: res = sum
    sharkdir = directions[map[cord[0]][cord[1]][1]%8]
    newmap = copy.deepcopy(map)
    newmap[cord[0]][cord[1]][0] = -1
    newmap = fishmove(newmap)
    newmap[cord[0]][cord[1]] = [0,0]
    for i in range(1,4):
        y = cord[0] + sharkdir[0]*i
        x = cord[1] + sharkdir[1]*i
        if y < 0 or y > 3 or x < 0 or x > 3 or newmap[y][x][0] == 0: continue
        sharking(newmap, [y,x], sum)

# 맵 만들기
firstmap = [[] for _ in range(4)]
for row in range(4):
    r = list(map(int, input().split(" ")))
    firstmap[row] = [[r[0], r[1]], [r[2], r[3]], [r[4], r[5]], [r[6], r[7]]]

sharking(firstmap, [0,0], 0)
print(res)