# 백준 1967: 트리의 지름
# 2024.05.10(금) 스터디 과제

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline



# 입력받기

n = int(input()) # 노드의 개수



# 그래프 입력받기
graph = [[] for _ in range(n + 1)]  # 가중치 그래프 만들기
for i in range(n - 1):
    parent, child, edge = map(int, input().split()) # 부모, 자식, 간선 정보 입력받기
    graph[parent].append((child, edge)) # 부모 노드 기준 연결관계 정의
    graph[child].append((parent, edge)) # 자식 노드 기준 연결관계 정의

# dfs 로직 준비
ends = [0,0] # 보고 있는 노드에서 (가장 먼 노드, 거리)를 갱신 및 저장
visited = [] # 방문기록 추적

def dfs(node, route):
    global visited # 전역변수 visited을 그대로 씀
    global ends # 전역변수 ends을 그대로 씀
    visited.append(node) # 방문표시
    visit_max = 1 
    
    for next in graph[node]:
        if next[0] not in visited: # node의 자식노드를 아직 방문하지 않은 경우
            visit_max = 0
            dfs(next[0], route + next[1])
    
    if visit_max == 1: # 마지막 노드에 도달한 경우에 ends와 비교해서 갱신 여부 결정
        if route > ends[1]: # 지금 경로가 최대 경로 길이보다 길면
            ends[0] = visited[-1] # 현재 방문한 노드를 먼점으로 지점
            ends[1] = route # 경로 길이 갱신
    visited.pop() # 스택에 가장 위의 점 pop
    return

dfs(1,0)
visited.clear()
dfs(ends[0], 0)
print(ends[1])

