# https://www.acmicpc.net/problem/25757
# 임스와 함께하는 미니게임

import sys
input = sys.stdin.readline

firstInput = input().split()
call = int(firstInput[0])
if firstInput[1] == "Y": game = 1
elif firstInput[1] == "F": game = 2
else: game = 3

callSet = set()
for _ in range(call):
    callSet.add(input())
print(len(callSet)//game)

# callDict = dict()
# for c in range(call):
#     user = input()
#     callDict[user] = c
# print(len(callDict)//game)