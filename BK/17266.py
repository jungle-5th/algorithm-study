import sys
import math

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())  # 굴다리 길이
M = int(input())  # 가로등 개수
x = list(map(int, input().split()))


def solution(N, M, locations):
    # 첫 번째 가로등과 굴다리 시작점 사이의 거리
    max_distance = locations[0]

    # 가로등 사이의 최대 거리의 절반
    for i in range(1, M):
        max_distance = max(
            max_distance, math.ceil((locations[i] - locations[i - 1]) / 2)
        )

    # 마지막 가로등과 굴다리 끝점 사이의 거리
    max_distance = max(max_distance, N - locations[-1])

    print(max_distance)


solution(N, M, x)
