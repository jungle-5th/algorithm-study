# 2024.05.25(토)
# 백준 11057: 오르막 수
# 주제: 다이나믹 프로그래밍

N = int(input())
dp_table = [1] * 10

for i in range(0, N):
    for j in range(8, -1, -1):
        dp_table[j] = dp_table[j] + dp_table[j + 1]

print(dp_table[0] % 10007)