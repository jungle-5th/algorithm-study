from sys import stdin
input = stdin.readline
def stack(n_numbers):
    answer = list()
    for _ in range(n_numbers):
        answer.append(int(input()))
    count = 0
    
    stack_list = list()
    output = list()
    for i in range(1, n_numbers+1):
        stack_list.append(i)
        output.append('+')
        if stack_list[len(stack_list)-1] == answer[count]:
            while stack_list and stack_list[len(stack_list)-1] == answer[count]:
                stack_list.pop()
                output.append('-')
                count += 1
    if count != n_numbers:
        print('NO')
        return
    for i in output:
        print(i)
    return

n_numbers = int(input())

stack(n_numbers)