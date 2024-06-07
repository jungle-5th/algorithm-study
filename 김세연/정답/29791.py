# 2024.06.07(금)
# 문제: 백준29791 https://www.acmicpc.net/problem/29791
# 주제: 구현, 정렬

from sys import stdin

input = stdin.readline


def sol():
    N, M = map(int, input().split())
    press_e = sorted([x for x in map(int, input().split())])
    press_o = sorted([x for x in map(int, input().split())])
    cnt_e = logic(press_e, 100, N)
    cnt_o = logic(press_o, 360, M)
    print(f"{cnt_e} {cnt_o}")


def logic(press, duration, number):
    cnt = 1
    start = press[0]
    cur = start

    if number == 1:
        return cnt

    for i in range(1, number):
        if press[i] - cur >= duration:
            cur = press[i]
            cnt += 1
    return cnt


sol()
