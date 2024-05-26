# 2024.05.22(수)
# 백준 20115: 에너지 드링크 https://www.acmicpc.net/problem/20115
# 주제: 그리디 알고리즘

import sys
from collections import deque

input = sys.stdin.readline


def sol():
    print(logic(inputs()))


# 입력값 받기
def inputs():
    N = int(input())
    drinks = [x for x in map(int, input().split())]

    return N, drinks


# 로직: 붕붕드링크 만들기
def logic(N, drinks):
    drinks.sort()  # 붕붕드링크 조제를 위해 정렬

    for i in range(N - 1):  # 처음부터 최대값전까지 순회하면서 붕붕드링크 조제
        drinks[-1] = drinks[-1] + drinks[i] / 2  # 최대값에 갱신

    return drinks[-1] # 최대값 반환


sol()
