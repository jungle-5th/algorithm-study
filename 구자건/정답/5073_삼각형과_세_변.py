from sys import stdin
input = stdin.readline

def judge(edge1, edge2, edge3):
    result1 = edge1 == edge2
    result2 = edge2 == edge3
    result3 = edge1 == edge3
    
    if edge1 + edge2 + edge3 <= 2 * max(edge1, edge2, edge3):
        return 'Invalid'
    if result1 and result2 and result3:
        return 'Equilateral'
    if result1 or result2 or result3:
        return 'Isosceles'
    return 'Scalene'

while True:
    edge1, edge2, edge3 = map(int, input().split(' '))
    if edge1 == 0:
        break
    print(judge(edge1, edge2, edge3))

