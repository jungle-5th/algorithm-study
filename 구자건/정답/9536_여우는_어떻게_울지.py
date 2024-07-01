from sys import stdin
input = stdin.readline

def what_does_the_fox_say():
    input_list = list(input().rstrip().split(' '))
    while 1:
        input_line = input().rstrip()
        if input_line == 'what does the fox say?':
            break
        input1, input2, input3 = input_line.split(' ')
        while input3 in input_list:
            input_list.remove(input3)
    
    print(*input_list)
    return

n_try = int(input())
for _ in range(n_try):
    what_does_the_fox_say()