## https://www.acmicpc.net/problem/1260
## DFS와 BFS

# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
# 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
# V부터 방문된 점을 순서대로 출력하면 된다.

# 예제 입력 1 
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# 예제 출력 1 
# 1 2 4 3
# 1 2 3 4


first_input = input().split(" ")
n_of_vertex = int(first_input[0])
m_of_edge = int(first_input[1])
start = int(first_input[2]) - 1

# adj_list 작성
adj_list = []
for i in range(n_of_vertex):
    adj_list.append([])
for i in range(m_of_edge):
    edge = input().split(" ")
    vertex_from = int(edge[0]) - 1
    vertex_to = int(edge[1]) - 1
    adj_list[vertex_from].append(vertex_to)
    adj_list[vertex_to].append(vertex_from)

# print(adj_list)

def dfs(adj_list):
    stack = [start]
    visited_list_dfs = []
    while stack:
        current_dfs = stack.pop(-1)
        if current_dfs in visited_list_dfs: continue
        print(current_dfs + 1, end=" ")
        visited_list_dfs.append(current_dfs)
        temp_list = []
        for i in adj_list[current_dfs]:
            if i not in visited_list_dfs:
                temp_list.append(i)
        temp_list.sort(reverse=True)
        stack.extend(temp_list)

def bfs(adj_list):
    que = [start]
    visited_list_bfs = []
    while que:
        current_bfs = que.pop(0)
        if current_bfs in visited_list_bfs: continue
        print(current_bfs + 1, end=" ")
        visited_list_bfs.append(current_bfs)
        temp_list = []
        for i in adj_list[current_bfs]:
            if i not in visited_list_bfs:
                temp_list.append(i)
        temp_list.sort()
        que.extend(temp_list)

dfs(adj_list)
print()
bfs(adj_list)