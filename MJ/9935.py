## https://www.acmicpc.net/problem/9935
## 문자열 폭발

# 문제
# 상근이는 문자열에 폭발 문자열을 심어 놓았다. 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.
# 폭발은 다음과 같은 과정으로 진행된다.
# 문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다.
# 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
# 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
# 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
# 상근이는 모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려고 한다.
# 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력한다.
# 폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.

# 입력
# 첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.
# 둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.
# 두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만 이루어져 있다.

# 출력
# 첫째 줄에 모든 폭발이 끝난 후 남은 문자열을 출력한다.

# 예제 입력 1 
# mirkovC4nizCC44
# C4
# 예제 출력 1 
# mirkovniz

# 예제 입력 2 
# 12ab112ab2ab
# 12ab
# 예제 출력 2 
# FRULA

string = list(input())
len_of_string = len(string)
bomb = list(input())
len_of_bomb = len(bomb)
if len_of_bomb > len_of_string:
    print("".join(string))
    exit()

result_stack = []
idx = 0


def check_and_explode():
    pushnumber = 1
    explosion = True
    if len_of_bomb > len(result_stack): return pushnumber
    for i in range(len_of_bomb):
        if result_stack[-1-i] != bomb[-1-i]:
            explosion = False
            pushnumber += i
            break
    if explosion == True:
        for _ in range(len_of_bomb): result_stack.pop(-1)
    return pushnumber

for _ in range(len_of_bomb):
    result_stack.append(string[idx])
    idx += 1
idx -= 1
pushnum = 0
while (idx < len_of_string):
    for _ in range(pushnum):
        idx += 1
        if idx < len_of_string: result_stack.append(string[idx])
    
    pushnum = check_and_explode()

if result_stack == []:
    print("FRULA")
else: print("".join(result_stack))



## 시간초과 코드
# search_index = len_of_bomb - 1
# while(search_index < len_of_string):
#     explosion = True
#     for i in range(len_of_bomb):
#         if string[search_index - i] != bomb[-1-i]:
#             explosion = False
#             search_index += i
#             break
#     if explosion == True:
#         search_index = search_index - len_of_bomb + 1
#         for _ in range(len_of_bomb): string.pop(search_index)
#         # print("boom")
#         len_of_string = len(string)
#     else: search_index += 1
# if string == []:
#     print("FRULA")
# else: print("".join(string))