## https://www.acmicpc.net/problem/7562
## 나이트의 이동

# 문제
# 체스판 위에 한 나이트가 놓여져 있다. 나이트가 이동하려고 하는 칸이 주어진다.
# 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

# 입력
# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
# 각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다.
# 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다.
# 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

# 출력
# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

# 예제 입력 1 
# 3
# 8
# 0 0
# 7 0
# 100
# 0 0
# 30 50
# 10
# 1 1
# 1 1

# 예제 출력 1
# 5
# 28
# 0

def zone(target_cord):
    x = max(abs(target_cord[0]), abs(target_cord[1]))
    y = min(abs(target_cord[0]), abs(target_cord[1]))
    return [x, y]
    

test_cases = int(input())
for _ in range(test_cases):
    n_of_square = int(input())
    position1 = list(map(int,input().split(" ")))
    position2 = list(map(int,input().split(" ")))
    target = [position2[0]-position1[0], position2[1]-position1[1]]

    ## 4X4에서 구석인 경우
    if n_of_square == 4 and (position1 in [[0,0],[0,3],[3,0],[3,3]]):
        if zone(target) == [3,0]:
            print(5)
            continue
    if (position1 in [[0,0],[n_of_square-1,0],[0,n_of_square-1],[n_of_square-1,n_of_square-1]]):
        if zone(target) == [1,1]:
            print(4)
            continue

    if target == [0,0]:
        print(0)
        continue
    target = zone(target)
    if target == [2,2]:
        print(4)
        continue
    target = [target[0]-2,target[1]-1]
    target = zone(target)
    count = 1

    while True:
        if target == [0,0]: break
        elif target == [1,0]:
            count += 1
            break
        else:
            target = [target[0]-2,target[1]-1]
            target = zone(target)
            count += 1
    
    print(count)