from sys import stdin
from collections import deque

input = stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(m,n,graph):
    start_row, start_col = 0, 0 # 상근이의 위치
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '@': # 상근이 정보 추가
                start_row, start_col = i,j
                queue.append((start_row, start_col, 0))
            elif graph[i][j] == '*': # 불 정보 추가
                queue.appendleft((i, j, 0))
    while queue:
        row, col, time = queue.popleft()
        if(row == 0 or row == n -1 or col == 0 or col == m - 1) and graph[row][col] == '@': # 종료조건
            return time + 1
        if graph[row][col] == '*': # 시간에 따른 불의 이동
            for i in range(4):
                now_row, now_col = row + dr[i], col+dc[i]
                if now_row < 0 or now_row >= n or now_col < 0 or now_col >= m : # 지도 밖인 경우
                    continue
                if graph[now_row][now_col] == '#':
                    continue
                if graph[now_row][now_col] == '.':
                    graph[now_row][now_col] = '*'
                    queue.append((now_row, now_col, time + 1))
        else:
            for i in range(4): # 시간에 따른 상근이의 이동
                now_row, now_col = row+dr[i], col+dc[i]
                if now_row < 0 or now_row >= n or now_col < 0 or now_col >= m : # 지도 밖인 경우
                    continue
                if graph[now_row][now_col] == '*' or graph[now_row][now_col] == '#': # 벽이나 불인 경우
                    continue
                if graph[now_row][now_col] == '.': # 빈 공간인 경우
                    graph[now_row][now_col] = '@'
                    queue.append((now_row, now_col, time + 1))
    return 'IMPOSSIBLE'

t = int(input())
for _ in range(t):
    m,n = map(int, input().rstrip().split())
    graph = [list(input().rstrip()) for _ in range(n)]
    print(bfs(m,n,graph))