# https://www.acmicpc.net/problem/13305
# 주유소

nOfCities = int(input())
distance = list(map(int, input().split()))
gasCost = list(map(int, input().split()))
minCost = 2000000000

sum = 0

for i in range(nOfCities-1):
    if minCost > gasCost[i]: minCost = gasCost[i]
    sum += distance[i]*minCost

print(sum)