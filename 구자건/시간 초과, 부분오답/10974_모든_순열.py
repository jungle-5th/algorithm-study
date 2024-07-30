from sys import stdin
input = stdin.readline

def every_sequence(number, output_list):
    if len(output_list) == number:
        print(*output_list)
    
    for i in range(1, number+1):
        next_output_list = output_list.copy()
        if not i in output_list:
            next_output_list.append(i)
            every_sequence(number, next_output_list)
    return

number = int(input())
output_list = list()
every_sequence(number, output_list)