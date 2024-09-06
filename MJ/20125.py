# https://www.acmicpc.net/problem/20125
# 쿠키의 신체 측정

nOfSquare = int(input())
heart = [0,0]
for i in range(nOfSquare):
    row = list(input().strip())
    for j in range(nOfSquare):
        if row[j] == "*": heart = [i+2, j+1]; break
    if heart != [0,0]: break
row = list(input().strip())
for i in range(heart[1]-1):
    if row[i] == "*": leftarm = heart[1]-1-i; break
rightarm = 0
for i in range(heart[1], nOfSquare):
    if row[i] == "*": rightarm +=1
    else: break

waist = 0
leftleg = 0
rightleg = 0
for i in range(heart[0], nOfSquare):
    row = input().strip()
    if row[heart[1]-1] == "*": waist +=1
    else:
        if row[heart[1]-2] == "*": leftleg +=1
        elif row[heart[1]] == "_": break
        if row[heart[1]] == "*": rightleg +=1

print(f"{heart[0]} {heart[1]}\n{leftarm} {rightarm} {waist} {leftleg} {rightleg}")