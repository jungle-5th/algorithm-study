# 겹치는건 싦어

import sys
input = sys.stdin.readline

n,k = map(int, input().split())

sequence = list(map(int, input().split()))
# print(sequence)

count = [0] * 1000000

end = 0
cnt = 0
maxCnt = 0

# 투 포인터 알고리즘
for start in range(n): # start -> n까지 증가

     # end가 수열범위내이고, 특정 원소 개수가 k개 이하이면 개수 증가
     while  end < n and count[sequence[end]] +1 <= k: 
          cnt +=1
          count[sequence[end]] +=1
          end +=1
          maxCnt = max(maxCnt, cnt)

     # 특정 원소 개수가 k개 초과하면 start증가하고, 특정 원소 카운트 감소
     count[sequence[start]] -=1 
     cnt -=1 # 부분 수열의 길이도 감소

print(maxCnt)
