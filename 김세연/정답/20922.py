import sys

input = sys.stdin.readline

N, K = map(int, input().split())


numbers = [x for x in map(int, input().split())]


# 포인터
l = 0
r = 0
result = 0


if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    k_table = {}
    l = 0
    result = 0

    for r in range(N):
        cur = numbers[r]
        if cur in k_table:
            k_table[cur] += 1
        else:
            k_table[cur] = 1

        while k_table[cur] > K:
            k_table[numbers[l]] -= 1
            l += 1
        result = max(result, r - l + 1)

    print(result)
