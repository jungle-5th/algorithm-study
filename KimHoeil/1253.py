# 1253번

import sys

input = sys.stdin.readline

n = int(input())

sequence = list(map(int, input().split()))
sequence.sort()

sum = 0
goodCnt = 0

for idx in range(n):
     start = 0
     end = n-1
     while True:
          if start == idx:
               start +=1
          if end == idx:
               end-=1
          if start == end:
               break

          sum = sequence[start]+ sequence[end]

          # 두수를 더한값이 좋다 인지 확인
          if sum == sequence[idx]:
               goodCnt+=1
               break
          elif sum > sequence[idx]:
               end -=1
          else:
               start +=1
                              
print(goodCnt)
     
               
          
          
