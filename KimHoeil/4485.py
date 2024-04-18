# 4485번
from collections import deque
import sys

input = sys.stdin.readline


def bfs(x,y,index):

     # 상하좌우
     dx = [-1,1,0,0]
     dy = [0,0,-1,1]

     q = deque()
     q.append((x,y))
     dis[x][y] = arr[x][y] # 시작지점 초기화

     while q:
          curx, cury = q.popleft()
          for i in range(4):
               nx = curx + dx[i]
               ny = cury + dy[i]
               
               if 0<=nx<n and 0<=ny<n and dis[nx][ny] > dis[curx][cury]+arr[nx][ny]:
                    q.append((nx,ny))
                    dis[nx][ny] = dis[curx][cury]+arr[nx][ny]
               
     
     print(f"Problem {index}: {dis[n-1][n-1]}")
     # for d in dis:
     #      print(d)
     # print()


idx = 1
while True:
     n = int(input())

     if n==0:
          break

     arr = []
     dis = [[1e9 for j in range(n)] for i in range(n)]

     for i in range(n):
          arr.append(list(map(int, input().split())))
     
     bfs(0,0,idx)
     idx+=1
