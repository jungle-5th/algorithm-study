# 30012번 세연이형식 풀이법

import sys

# sys.stdin = open('input.txt','r')
input = sys.stdin.readline


s,n = map(int, input().split())
E = list(map(int, input().split()))
k,l = map(int, input().split())


# print(E)

minJumpDis = k*2

distance = []
# 주호와 다른 개구리의 거리 계산
for i in E:
     dis = abs(s-i)
     distance.append(dis)
# print(distance)

costList = []
for dis in distance:
     if dis < 2*k: # 개구리간의 거리가 2k 미만인 경우
          jumpCost = 2*k - dis
          costList.append(jumpCost)

     else: # 개구리간의 거리가 2K이상이거나 2K인 경우
          walkCost = l * (dis-2*k)
          costList.append(walkCost)

minCost = min(costList)
index = costList.index(minCost) +1 
print(minCost, index)

# 30012번 자건식 풀이법

import sys

# sys.stdin = open('input.txt','r')
input = sys.stdin.readline


s,n = map(int, input().split())
E = list(map(int, input().split()))
k,l = map(int, input().split())


minJumpDis = k*2

distance = []
# 주호와 다른 개구리의 거리 계산
for i in E:
     dis = abs(s-i)
     distance.append(dis)

costList = []
for dis in distance:
     cost = 0
     for _ in range(2):       # 점프 두번하고 남은거리 걸어가기
          move = min(k, dis)  # k만큼 점프하거나, 남은거리만큼 점프하기
          cost += abs(move-k) # 점프 비용 계산
          dis -= move         # 남은거리 갱신
     cost += l * dis          # 점프하고 남은 거리 걸어가기
     costList.append(cost)


minCost = min(costList)
index = costList.index(minCost) + 1
print(minCost, index)


