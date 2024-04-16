## https://www.acmicpc.net/problem/22866
## 탑 보기

# 문제
# 일직선으로 다양한 높이의 건물이 총 N개가 존재한다. 각 건물 옥상에서 양 옆에 존재하는 건물의 옆을 몇 개 볼 수 있는지 궁금해졌다. 
# i번째 건물 기준으로 
# i - 1, i - 2, ..., 1번째 건물은 왼쪽에, 
# i + 1, i + 2, ..., N번째 건물은 오른쪽에 있다. 각 건물 사이의 거리는 다 동일하다.

# 현재 있는 건물의 높이가 L이라고 가정하면 높이가 L보다 큰 곳의 건물만 볼 수 있다.
# 바라보는 방향으로 높이가 L인 건물 뒤에 높이가 L이하인 건물이 있다면 가려져서 보이지 않는다.

# 번호	1	2	3	4	5	6	7	8
# 높이	3	7	1	6	3	5	1	7
# 보이는 건물 번호	2	x	2, 4, 8	2, 8	2,4,6,8	2,4,8	2,4,6,8	x
# 각 건물에서 볼 수 있는 건물들이 어떤것이 있는지 구해보자.

# 입력
# 첫번째 줄에 건물의 개수 N이 주어진다.
# 두번째 줄에는 N개의 건물 높이가 공백으로 구분되어 주어진다.

# 출력
# i번째 건물에서 볼 수 있는 건물의 개수를 출력한다.

# 만약 볼 수 있는 건물의 개수가 1개 이상이라면 
# i번째 건물에서 거리가 가장 가까운 건물의 번호 중 작은 번호로 출력한다.

# 제한
# 1 <= N <= 100,000
# 1 <= L <= 100,000
# 예제 입력 1 
# 8
# 3 7 1 6 3 5 1 7
# 예제 출력 1 
# 1 2
# 0
# 3 2
# 2 2
# 4 4
# 3 4
# 4 6
# 0
import sys
n_of_tower = int(input())
towers = list(map(int, sys.stdin.readline().split(" ")))
towers.insert(0,0)

## DP테이블은 각 인덱스 탑에 대해서 [가장 가까운 나보다 큰 탑의 인덱스, 내가 볼 수 있는 탑의 갯수]
# 오른쪽 끝부터 채우는 테이블과 왼쪽 끝부터 채우는 테이블이 있고 나중에 둘을 결합한다.

dp_r_table = [[300000,0] for _ in range(n_of_tower+1)]
for i in range(n_of_tower-1,0,-1): # 오른쪽 끝부터 타워를 보면서 나보다 오른쪽에 더 큰 타워가 있는지 확인
    j = i+1
    while j!= 300000:
        if towers[i] < towers[j]: # 더 큰게 보이면 dp_r_table 업데이트.
            dp_r_table[i] = [j,dp_r_table[j][1]+1] # 보이는 탑의 갯수는 첫번쨰로 보이는 탑이 보고있는 갯수 + 1
            break
        else: j = dp_r_table[j][0]


# 마찬가지로 왼쪽 끝부터 왼쪽을 보면서 채우는 DP테이블 실행
dp_l_table = [[-300000,0] for _ in range(n_of_tower+1)]
for i in range(2,n_of_tower+1,1):
    j = i-1
    while j!= -300000:
        if towers[i] < towers[j]: # 더 큰게 보이면 dp_r_table 업데이트.
            dp_l_table[i] = [j,dp_l_table[j][1]+1] # 보이는 탑의 갯수는 첫번쨰로 보이는 탑이 보고있는 갯수 + 1
            break
        else: j = dp_l_table[j][0]

for i in range(1, n_of_tower+1, 1):
    see_count = dp_r_table[i][1] + dp_l_table[i][1]
    if see_count == 0: print(0)
    else:
        if (i-dp_l_table[i][0] <= dp_r_table[i][0]-i): print(f"{see_count} {dp_l_table[i][0]}")
        else: print(f"{see_count} {dp_r_table[i][0]}")