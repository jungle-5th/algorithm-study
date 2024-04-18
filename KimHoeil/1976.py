# 1976번

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

city = []
for i in range(n):
     city.append(list(map(int, input().split())))

for i in range(n):
     for j in range(n):
          if i!=j and city[i][j] == 0: city[i][j] = 1e10

# for i in city:
#      print(i)

tourList = list(map(int, input().split()))

def floyd(n):
     for k in range(n):
          for i in range(n):
               for j in range(n):
                    if city[i][k] + city[k][j] < city[i][j]:
                         city[i][j] = city[i][k] + city[k][j]

     # for i in city:
     #      print(i)

floyd(n)

flag = False
for i in range(m-1):
     if city[tourList[i] -1][tourList[i+1] -1] == 1e10:
          print("NO")
          flag = True
          break

if flag == False:
     print("YES")
          
               
