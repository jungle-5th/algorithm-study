from sys import stdin

def lotto(number_list, cur_list):
    if len(cur_list) == 6:
        print(*cur_list)
        return
    for i in number_list:
        if 0<len(cur_list) and i < cur_list[-1]:
            continue
        
        next_cur_list = cur_list.copy()
        next_number_list = number_list.copy()
        next_cur_list.append(i)
        next_number_list.remove(i)
        lotto(next_number_list, next_cur_list)
    return

while True:
    
    input_line = input()
    if input_line == '0': break
    
    input_line = list(map(int, input_line.split(' ')))
    n_number = input_line[0]
    number_list = input_line[1:]
    lotto(number_list, list())
    print()
