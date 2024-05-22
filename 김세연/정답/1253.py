# 백준 1253: 좋다!

import sys

input = sys.stdin.readline

"""입력받기"""
N = int(input())

n_list = [x for x in map(int, input().split())]

"""로직"""
n_list.sort() # 정렬해주기

if N < 3: # 원소가 2개 이하면 0 반환
    print(0)
else: # 원소가 3개 이상일 때
    count, sum = 0, 0
    target, left, right = 0, 1, N - 1
    while target < len(n_list):  # 전 구간 순회
        sum = n_list[left] + n_list[right] 
        if left == right: #  포인터가 겹칠 때 다음 타겟
            target += 1
            left = 0
            right = N - 1
        elif left == target or sum < n_list[target]:
            left += 1
        elif right == target or sum > n_list[target]:
            right -= 1
        elif sum == n_list[target]: # 타겟을 만날 경우 좋은 수 1개 추가
            count += 1
            target += 1
            left = 0
            right = N - 1
    print(count)
