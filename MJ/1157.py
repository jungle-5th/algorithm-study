# https://www.acmicpc.net/problem/1157
# 단어 공부
# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 예제 입력 1 
# Mississipi
# 예제 출력 1 
# ?
# 예제 입력 2 
# zZa
# 예제 출력 2 
# Z
# 예제 입력 3 
# z
# 예제 출력 3 
# Z

s = list(input().strip())
alphabet = [0]*26
for i in s:
    if ord(i) < 91: alphabet[ord(i)-65] += 1
    else: alphabet[ord(i)-97] += 1
max = [0,0]
for count in range(26):
    if max[0] < alphabet[count]: max[0] = alphabet[count]; max[1] = count
for i in range(max[1]+1,26):
    if alphabet[i] == max[0]: print("?"); exit()
print(chr(max[1]+65))