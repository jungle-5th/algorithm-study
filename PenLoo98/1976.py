import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
# 도시의 수
city_info = []
for _ in range(n):
    city_info.append(list(map(int,input().split())))

# 여행 갈 순서
plan = list(map(int,input().split()))

# 건너건너 연결된 도시를 찾기 
for k in range(n):
    for i in range(n):
        for j in range(n):
            if city_info[i][k] and city_info[k][j]:
                city_info[i][j]=1

# 계획한 도시 순서대로 이동가능한지 확인하기 
can_visit = "YES"
start=plan[0]-1
for target in plan:
    next=target-1
    if start==next:
        continue
    if not city_info[start][next]:
        can_visit="NO"
    start=next
print(can_visit)