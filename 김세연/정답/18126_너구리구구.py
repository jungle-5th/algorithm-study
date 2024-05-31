import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(node, count): 
    global total
    visit[node] = True
    
    for i, j in tree[node]:
        if not visit[i]:
            total = max(total, count + j)
            dfs(i, count + j)

n = int(input())
tree = [[]for _ in range(n + 1)]

for i in range(n-1):
    a,b,c = map(int, input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

visit = [False] *( n + 1)

total = 0
dfs(1, 0)

print(total)