from sys import stdin
input = stdin.readline

def akaraka(input_line):
    if len(input_line) == 0:
        return 'AKARAKA'
    
    line_length = len(input_line)
    k = line_length//2
    for i in range(k):
        if input_line[i] != input_line[-1-i]: return 'IPSELENTI'
    next_input_line = input_line[0 : k]
    return akaraka(next_input_line)

input_line = list(input().rstrip())
print(akaraka(input_line))