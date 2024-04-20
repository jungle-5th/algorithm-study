import sys
from collections import deque
input=sys.stdin.readline


def bfs_get_min_move(startX, startY, endX, endY):
    if(startX==endX and startY==endY):
        return print(0)

    # visited: 보드 판 방문
    visited=[[False]*I for _ in range(I)]
    
    # 체스판 이동 경우의 수
    dx=[2,2,1,1,-1,-1,-2,-2]
    dy=[1,-1,2,-2,2,-2,1,-1]

    # 체스판 시작지점 
    destination=deque([(startX,startY,0)])
    visited[startY][startX]=True

    # 이동지
    while(destination):
        # 시작 좌표
        x,y,move=destination.popleft()

        if(x==endX and y==endY):
            return print(move)  
        
        # 나이트 이동 8방향 탐색
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            # 보드 판의 좌표를 벗어나 있다면
            if(not(0<=nx<I) or not(0<=ny<I)):
                continue
            # 보드 판에 처음 방문했으면 
            if(not visited[ny][nx]):
                visited[ny][nx]=True
                destination.append((nx,ny,move+1))
            # 도착지점에 도착했으면
            if(nx==endX and ny==endY):
                break

# 테스트 케이스 처리 
t = int(input())
for _ in range(t):
    # 체스판 크기 
    I = int(input())
    # 시작 좌표 
    startX, startY=map(int,input().split())
    # 도착 좌표 
    endX, endY=map(int,input().split())

    bfs_get_min_move(startX, startY, endX, endY)