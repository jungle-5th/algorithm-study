# https://www.acmicpc.net/problem/1522
# 문자열 교환

# 문제
# a와 b로만 이루어진 문자열이 주어질 때,  a를 모두 연속으로 만들기 위해서 필요한 교환의 회수를 최소로 하는 프로그램을 작성하시오.
# 이 문자열은 원형이기 때문에, 처음과 끝은 서로 인접해 있는 것이다.
# 예를 들어,  aabbaaabaaba이 주어졌을 때, 2번의 교환이면 a를 모두 연속으로 만들 수 있다.

# 입력
# 첫째 줄에 문자열이 주어진다. 문자열의 길이는 최대 1,000이다.

# 출력
# 첫째 줄에 필요한 교환의 회수의 최솟값을 출력한다.

# 예제 입력 1 
# abababababababa
# 예제 출력 1 
# 3
# 예제 입력 2 
# ba
# 예제 출력 2 
# 0
# 예제 입력 3 
# aaaabbbbba
# 예제 출력 3 
# 0
# 예제 입력 4 
# abab
# 예제 출력 4 
# 1
# 예제 입력 5 
# aabbaaabaaba
# 예제 출력 5 
# 2
# 예제 입력 6 
# aaaa
# 예제 출력 6 
# 0

str = list(input().strip())
bs = []
bcount = 0
for i in range(len(str)):
    if str[i] == "b":
        bs.append(i)
        bcount += 1
if bcount == 0: print(0); exit()
minval = 10000000
for b in bs:
    acount = 0
    for i in range(bcount-1):
        if str[(b+1+i)%len(str)] == "a":
            acount += 1
    if minval > acount: minval = acount
print(minval)