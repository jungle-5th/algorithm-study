from sys import stdin
input = stdin.readline
def cutting_lan(n_line, n_target):
    line_list = list()
    sum = 0
    middle = 0
    for i in range(n_line):
        line_length = int(input())
        line_list.append(line_length)
        sum += line_length

    lp = 1
    rp = (sum // n_target) + 1
    result_condition = 0
    while(lp<=rp):
        n_cut_lines = 0
        middle = (lp + rp) // 2
        
        for i in range(n_line):
            n_cut_lines += line_list[i]//middle
        if n_cut_lines < n_target :
            rp = middle -1
        else:
            lp = middle +1
            result_condition = max(result_condition, middle)
    return result_condition

n_line, n_target = map(int, input().split(' '))
print(cutting_lan(n_line, n_target))