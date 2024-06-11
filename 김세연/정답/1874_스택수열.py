
from sys import stdin
input = stdin.readline

# 입력값 받기
n = int(input())  # 스택에 넣을 숫자(1 ~ n)
my_stack = [0]  # 스택
result = []  # 스택 동작과정 기록
sequence = [int(input()) for _ in range(n)]
my_numbers = [x for x in range(1, n + 1)]
current = 1  # 이때까지 넣은 숫자
possible = True

# 스택동작과정
# sequence와 비교하면서 스택에 넣고 빼기
for i in range(n):
    # if my_stack[len(my_stack) - 1] < sequence[i]:
    if my_stack[-1] < sequence[i]:
        
        # 수열의 문자까지 숫자를 스택에 넣기
        while current <= sequence[i]:
            my_stack.append(current)
            current += 1
            result.append("+")
        # 숫자를 다 넣은 다음 수열에서 일치하는 부분 pop 하고 '-' 찍기
        my_stack.pop()
        result.append("-")
    # elif my_stack[len(my_stack) - 1] == sequence[i]:
    elif my_stack[-1] == sequence[i]:
        my_stack.pop()
        result.append("-")
    else:
        possible = False
        result = "NO"
        break

if possible:
    for op in result:
        print(op)
else:
    print(result)
