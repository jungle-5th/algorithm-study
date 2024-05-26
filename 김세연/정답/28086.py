# 2024.05.11(토)
# 미소녀 컴퓨터 파루빗토 짱

import sys
input = sys.stdin.readline


def sol():
    equation = exp()
    operate(equation)


# 표현식 받기
def exp()-> tuple:
    expression = input().strip() # 표현식 자체를 입력받기
    op, A, B = '', '', ''
    for i in range(1, len(expression)):
        c = expression[i:i+1]
        if c == '+' or c == '-' or c =='*' or c == '/':
            op = c
            A = expression[:i]
            B = expression[i+1:]
            break
    return (A, op, B)

# 8진수 사칙연산
def operate(expression:tuple):
    A, op, B = expression
    A = int(A, 8)
    B = int(B, 8)
    C = 0
    
    if op == '+':
        C = A + B
    elif op == '-':
        C = A - B
    elif op == '*':
        C = A * B        
    elif op == '/':
        if B == 0:
            print("invalid")
            return
        C = A // B
    
    if C < 0:
        print('-' + oct(C)[3:])
    else:
        print(oct(C)[2:])



sol()
