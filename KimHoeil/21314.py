# 21314번

import sys
import copy

input = sys.stdin.readline

minGuyeomSoo = list(input())
maxMinguyeomSoo = copy.deepcopy(minGuyeomSoo)

# for s in minGuyeomSoo:
#      print(s)
# print()

maxList = ''
minList = ''

# for cur in range(len(minGuyeomSoo)):
cur = 0
# 최댓값 구하기
while cur < len(maxMinguyeomSoo):

     if maxMinguyeomSoo[cur] == 'M':
          # print(cur)
          try:
               idx = maxMinguyeomSoo.index('K')
          except:
               idx = 0
          maxMinguyeomSoo[idx] = 0
          # print(idx)
          # print("cur idx", cur, idx)

          # K가 string에 없다면 M만 있다는 뜻
          if idx == 0:
               idx = len(maxMinguyeomSoo)
               string = ''
               for i in range(cur, idx):
                    string += '1'
               maxList += string
               break
          else:
               count = 0
               for i in range(cur, idx):
                    count +=1
               
               string = '5'
               for i in range(count):
                    string += '0'
               
               # print(string)
               cur = idx
               maxList += string
               continue

     # cur == K인 경우
     elif maxMinguyeomSoo[cur] == 'K': 
          maxMinguyeomSoo[cur] = 0
          maxList += '5'
     cur+=1


cur = 0
# 최소값 구하기
while cur < len(minGuyeomSoo):

     if minGuyeomSoo[cur] == 'M':
          try:
               idx = minGuyeomSoo.index('K')
          except:
               idx = 0
          
          # K가 string에 없다면 M만 있다는 뜻
          if idx == 0:
               idx = len(minGuyeomSoo)
               count = 0
               for i in range(cur, idx-1):
                    count +=1
               
               string = '1'
               for i in range(count):
                    string += '0'
               minList += string
               break
          else:
               count = 0
               for i in range(cur, idx-1):
                    count +=1
               
               string = '1'
               for i in range(count):
                    string += '0'
               
               # print(string)
               cur = idx
               minList += string
               continue

     # cur == K인 경우
     elif minGuyeomSoo[cur] == 'K': 
          minGuyeomSoo[cur] = 0
          minList += '5'

     cur+=1

print(maxList)
print(minList)
