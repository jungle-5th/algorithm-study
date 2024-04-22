## https://www.acmicpc.net/problem/15732
## 도토리 숨기기

# 문제
# HEPC 1등 상금으로 도토리 D개를 받은 욕심많은 다람쥐 수형이는 자신의 모든 도토리를 뺏기지 않게 보관하려고 한다.
# 수형이는 1부터 N까지의 번호가 붙여있는 N개의 상자를 가지고 있고 이 안에 도토리를 넣어 다른 다람쥐들이 찾지 못하게 전부 숨기려고 한다.
# 상자가 너무 많아 도토리가 있는 상자를 모두 외울 수 없는 수형이는
# A번 상자부터 B번 상자까지 C개 간격으로 도토리를 하나씩 더 넣는 규칙을 만들었다!
# 다른 다람쥐들이 규칙을 눈치채고 모든 도토리를 잃는 것이 무서운 나머지
# 이러한 규칙들을 K개를 만들어 도토리를 최대한 안전하게 저장해 놓으려고 한다.
# 예를 들어 100번 상자부터 150번상자까지 10개 간격으로, 110번 상자부터 150번 상자까지 15개 간격으로 넣는다면
# 100, 110, 120, 125, 130, 140, 150번 상자에 도토리가 있으며 110번 상자와 140번 상자에는 2개의 도토리가 들어가 있게 된다.
# 상자 하나에 들어갈 수 있는 도토리의 개수는 제한이 없으며
# 앞의 상자부터 최대한 꽉꽉 채워나간다고 했을 때 마지막 도토리가 들어가 있는 상자의 번호를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 상자의 개수 N(1 ≤ N ≤ 1,000,000)과 규칙의 개수 K(1 ≤ K ≤ 10,000),
# 도토리의 개수 D(1 ≤ D ≤ 1,000,000,000)가 주어진다.
# 그 후 K개 줄에는 A, B, C(1 ≤ C ≤ A ≤ B ≤ N)가 주어지며
# A번 상자부터 B번 상자까지 C개 간격으로 도토리를 하나씩 넣는 규칙을 뜻한다.
# D는 모든 규칙으로 넣을 수 있는 도토리의 수보다 같거나 작다.

# 출력
# D개의 도토리를 규칙에 맞게 상자 앞에서부터 넣었을 때 마지막 도토리가 들어가는 상자의 번호를 출력하시오.

# 예제 입력 1 
# 200 2 5
# 100 150 10
# 110 150 15
# 예제 출력 1 
# 125

import sys
import math

def squirrel(rules, boxnum):
    dotori = 0
    for rule in rules:
        if rule[1] <= boxnum: dotori += ((rule[1]-rule[0])//rule[2] + 1)
        elif rule[0] > boxnum: continue
        else:
            i = 0
            while rule[0]+i < boxnum:
                dotori += 1
                i += rule[2]
    return dotori

first_input = input().split(" ")
n_of_boxes = int(first_input[0])
k_of_rules = int(first_input[1])
d_of_dotori = int(first_input[2])
boxes = [0] * (n_of_boxes + 1)
rules = []
for _ in range(k_of_rules):
    rule = list(map(int, sys.stdin.readline().split(" ")))
    rules.append(rule)

for rule in rules:
    for i in range((rule[1]-rule[0])//rule[2]+1):
        boxes[rule[0]+i*rule[2]] += 1
j=1
while(d_of_dotori>0):
    d_of_dotori -= boxes[j]
    j+=1

print(j-1)

# start = 0
# end = n_of_boxes
# boxnum = math.ceil((start+end)/2)
# while True:
#     dotori = squirrel(rules,boxnum)
#     temp = boxnum
#     if dotori < d_of_dotori:
#         start = boxnum
#     else:
#         end = boxnum
#     boxnum = math.ceil((start+end)/2)
#     if temp == boxnum:
#         print(boxnum-1)
#         break

