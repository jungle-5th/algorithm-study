import sys
input = sys.stdin.readline

n = int(input())
city_height = [0]+list(map(int,input().split()))

# 볼 수 있는 건물의 수 확인
leftStack = [] 
leftCount = [0]*(n+1) # 왼쪽을 본 수
minLeftViewIndex = [float('inf')]*(n+1)

rightStack = []
rightCount = [0]*(n+1)
minRightViewIndex = [float('inf')]*(n+1)

# 오른쪽으로 문워크하면서 왼쪽 확인
leftStack.append((city_height[1],1))
for i in range(2,n+1):
    stackTopHeight = leftStack[-1][0]
    currentHeight = city_height[i]
    # peek로 맨 위를 확인해 현재 높이보다 높은 높이가 나올때까지 pop
    while currentHeight >= stackTopHeight:
        leftStack.pop()
        if len(leftStack)!=0:
            stackTopHeight = leftStack[-1][0]
        elif len(leftStack)==0:
            break
    # 높은 높이가 나오면 Stack.size만큼 count 증가
    leftCount[i]+=len(leftStack)

    # 볼 수 있는 최소 인덱스 갱신
    if len(leftStack)!=0:
        minLeftViewIndex[i] = min(minLeftViewIndex[i], leftStack[-1][1])

    # 현재 높이를 Stack에 push
    leftStack.append((currentHeight,i))
    
    
# 왼쪽으로 문워크하면서 오른쪽 확인
rightStack.append((city_height[-1],n))
for i in reversed(range(1,n)):
    stackTopHeight = rightStack[-1][0]
    currentHeight = city_height[i]
    # peek로 맨 위를 확인해 현재 높이보다 높은 높이가 나올때까지 pop
    while currentHeight >= stackTopHeight:
        rightStack.pop()
        if len(rightStack)!=0:
            stackTopHeight = rightStack[-1][0]
        elif len(rightStack)==0:
            break
    # 높은 높이가 나오면 Stack.size만큼 count 증가
    rightCount[i]+=len(rightStack)

    # 볼 수 있는 최소 인덱스 갱신
    if len(rightStack)!=0:
        minRightViewIndex[i] = min(minRightViewIndex[i], rightStack[-1][1])

    # 현재 높이를 Stack에 push
    rightStack.append((currentHeight,i))

# 결과 출력 
for i in range(1,n+1):
    sumView = leftCount[i]+rightCount[i]
    # 인덱스 다시 처리하기 
    if (abs(i-minLeftViewIndex[i]) < abs(i-minRightViewIndex[i])):
        minViewIndex = minLeftViewIndex[i]
    elif (abs(i-minLeftViewIndex[i]) > abs(i-minRightViewIndex[i])):
        minViewIndex = minRightViewIndex[i]
    else:
        minViewIndex = min(minLeftViewIndex[i],minRightViewIndex[i])
    
    if sumView==0:
        print(sumView)
    else:
        print(sumView, minViewIndex)