from sys import stdin
import copy
input = stdin.readline

def comb(sequence, num_list, index):
    if not num_list:
        return 1
    count = 0
        
    for num in num_list:
        if index + num + 1 < len(sequence):
            if (not sequence[index]) and (not sequence[index + num + 1]):
                temp = copy.deepcopy(sequence)
                temp[index] = num
                temp[index + num + 1] = num
                
                temp_list = copy.deepcopy(num_list)
                temp_list.remove(num)
                if not 0 in temp:
                    count += 1
                else:
                    next_index = temp.index(0)
                    count += comb(temp, temp_list, next_index)
    return count

def solve(n_number, same_index1, same_index2):
    sequence = [0 for i in range(n_number*2)]
    num_list = [i for i in range(1, n_number+1)]
    sub = abs(same_index1 - same_index2)
    sequence[same_index1] = sub - 1
    sequence[same_index2] = sub - 1
    num_list.remove(sub - 1)
    next_index = sequence.index(0)
    return comb(sequence, num_list, next_index)

n_number, same_index1, same_index2 = map(int, input().split(' '))
print(solve(n_number, same_index1-1, same_index2-1))