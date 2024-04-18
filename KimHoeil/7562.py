#17837번

import sys
from collections import deque
input = sys.stdin.readline
t = int(input())



def bfs(x,y, goalX, goalY, board, visited):

     # 나이트의 다음 이동 방향
     dx = [-2,-2,-1,-1,1,1,2,2]
     dy = [-1,1,-2,2,-2,2,-1,1]

     q = deque()
     q.append((x,y))

     visited[x][y] = True
     while q:
          curX, curY = q.popleft()
          
          for i in range(8):
               nx = curX + dx[i]
               ny = curY + dy[i]
               
               if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] is False:
                         q.append((nx,ny))
                         visited[nx][ny] = True
                         board[nx][ny] = board[curX][curY] + 1

     print(board[goalX][goalY])

for i in range(t):
     n = int(input())
     initX, initY = map(int, input().split())
     goalX, goalY = map(int, input().split())
     
     board = [[0 for j in range(n)] for i in range(n)]
     visited = [[False for j in range(n)] for i in range(n)]
     bfs(initX,initY,goalX,goalY ,board, visited)
