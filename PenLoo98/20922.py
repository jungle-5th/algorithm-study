import sys
input = sys.stdin.readline

n,k = map(int,input().split())
array = list(map(int,input().split()))

numbers = [0]*100002
length = 0
answer = 0
left=0
right=0
for num in array:
    numbers[num]+=1
    if(numbers[num]>k):
        answer = max(answer,right-left)

        # 겹치는 수를 찾을 때까지 left를 이동
        while(array[left]!=num):
            # 빠지는 인덱스의 경우의 수 값 빼기
            numbers[array[left]]-=1
            left+=1
            length-=1
        numbers[array[left]]-=1
        left+=1
        right+=1
    else:
        right+=1
        length+=1
answer=max(answer,right-left)
print(answer)