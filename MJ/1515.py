# https://www.acmicpc.net/problem/1515
# 수 이어 쓰기

# 문제
# 세준이는 1부터 N까지 모든 수를 차례대로 공백없이 한 줄에 다 썼다.
# 그리고 나서, 세준이가 저녁을 먹으러 나간 사이에 다솜이는 세준이가 쓴 수에서 마음에 드는 몇 개의 숫자를 지웠다.
# 세준이는 저녁을 먹으러 갔다 와서, 자기가 쓴 수의 일부가 지워져있는 모습을 보고 충격받았다.
# 세준이는 수를 방금 전과 똑같이 쓰려고 한다. 하지만, N이 기억이 나지 않는다.
# 남은 수를 이어 붙인 수가 주어질 때, N의 최솟값을 구하는 프로그램을 작성하시오. 아무것도 지우지 않을 수도 있다.

# 입력
# 첫째 줄에 지우고 남은 수를 한 줄로 이어 붙인 수가 주어진다. 이 수는 최대 3,000자리다.

# 출력
# 가능한 N 중에 최솟값을 출력한다.

# 예제 입력 1 
# 1234
# 예제 출력 1 
# 4
# 예제 입력 2 
# 234092
# 예제 출력 2 
# 20
# 예제 입력 3 
# 999909
# 예제 출력 3 
# 49
# 예제 입력 4 
# 82340329923
# 예제 출력 4 
# 43
# 예제 입력 5 
# 32098221
# 예제 출력 5 
# 61
# 예제 입력 6 
# 1111111
# 예제 출력 6 
# 14
# 예제 입력 7 
# 00000000000000000000000000000000000000000000000000000000000000000000000
# 예제 출력 7 
# 400
# 예제 입력 8 
# 345029834023049820394802334909240982039842039483294792934790209
# 예제 출력 8 
# 279

num = 1
inputstr = ""
idx = 0
def check(start):
    global inputstr, num, idx
    if idx == len(inputstr): print(num); exit()
    numstr = str(num)
    for i in range(start, len(numstr)):
        if numstr[i] == inputstr[idx]:
            idx += 1
            check(i+1)
            break

inputstr = input().strip()
while idx < len(inputstr): check(0); num +=1