import sys
input = sys.stdin.readline

good_count=0
n=int(input())
numbers = list(map(int,input().split())) 
numbers.sort()

# 같은게 하나라도 있으면 True, 없으면 False
def is_good_number(numberList:list, search_number:int, search_number_index:int):
    left=0
    right=len(numberList)-1

    while(left!=right):
        # left+right=sumNumber sumNumber 구한다. 
        sum_number = numberList[left]+numberList[right]

        # sumNumber 찾는 수랑 같으면서 left,right가 search_number_index랑 다르면 True 반환
        if sum_number==search_number:
            if left != search_number_index and right != search_number_index:
                return True
            if left == search_number_index:
                left+=1
            elif right == search_number_index:
                right-=1

        # sumNumber가 찾는 수보다 크면 -> 줄인다. -> right-=1
        elif sum_number > search_number:
            right-=1

        # sumNumber가 찾는 수보다 작으면 -> 크게한다. -> left+=1
        elif sum_number < search_number:
            left+=1    
    return False

for i in range(0,len(numbers)):
    # 찾을 숫자를 저장하고
    search_number = numbers[i]
    # 좋은 숫자인지 판단하기 
    if is_good_number(numbers,search_number,i):
        good_count+=1
print(good_count)