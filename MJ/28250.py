# https://www.acmicpc.net/problem/28250
# 이브, 프시케 그리고 푸른 MEX의 아내

import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))
count_zero, count_one, count_other = 0,0,0

for i in range(n):
    if arr[i]==0: count_zero+=1
    elif arr[i]==1: count_one+=1
    else: count_other+=1
print(int(count_zero*(count_zero-1)/2+count_one*count_zero*2+count_other*count_zero))