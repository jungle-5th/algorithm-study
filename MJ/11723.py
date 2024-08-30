# https://www.acmicpc.net/problem/11723
# 집합

# 문제
# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

# 입력
# 첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
# 둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

# 출력
# check 연산이 주어질때마다, 결과를 출력한다.

import sys
nOfOrder = int(sys.stdin.readline())
s = set()
for _ in range(nOfOrder):
    order = sys.stdin.readline().strip().split()
    if order[0] == "add": s.add(order[1])
    elif order[0] == "remove": s.discard(order[1])
    elif order[0] == "check": print((order[1] in s)*1)
    elif order[0] == "toggle":
        if order[1] in s: s.discard(order[1])
        else: s.add(order[1])
    elif order[0] == "all": s = set({"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"})
    else: s = set({})
