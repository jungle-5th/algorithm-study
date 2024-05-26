import sys

input = sys.stdin.readline


def sol():
    N = int(input())
    dp = [0] * 11
    dp[1] = 0
    dp[2] = 2

    if N > 2:
        for i in range(3, N + 1):
            dp[i] = 3 * dp[i - 1]

    print(dp[N])


sol()
