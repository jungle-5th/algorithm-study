from sys import stdin

def is_num_list_good(num_list, list_size):
    count = 0
    for lp in range(list_size):
        for rp in range(lp+1, list_size):
            target = num_list[lp] + num_list[rp]
            find_left_pointer = 0
            find_right_pointer = list_size-1
            
            while(find_left_pointer<=find_right_pointer):
                find_pointer = (find_left_pointer + find_right_pointer)//2
                if target < num_list[find_pointer]:
                    find_right_pointer = find_pointer -1
                    continue
                if num_list[find_pointer] < target:
                    find_left_pointer = find_pointer +1
                    continue
                find_left_pointer = find_pointer-1
                find_right_pointer = find_pointer+1
                
                if find_pointer != lp and find_pointer !=rp:
                    if not is_counted[find_pointer]:
                        count += 1
                        is_counted[find_pointer] = True
                while(0 <= find_left_pointer and num_list[find_left_pointer] == target):
                    if find_left_pointer != lp and find_left_pointer !=rp:
                        if not is_counted[find_left_pointer]:
                            count += 1
                            is_counted[find_left_pointer] = True
                    find_left_pointer-=1
                while(find_right_pointer<list_size and num_list[find_right_pointer] == target):
                    if find_right_pointer != lp and find_right_pointer !=rp:
                        if not is_counted[find_right_pointer]:
                            count += 1
                            is_counted[find_right_pointer] = True
                    find_right_pointer+=1
                break
    return count

list_size = int(stdin.readline())
num_list = list(map(int, stdin.readline().split(' ')))
is_counted = [False for _ in range(list_size)]
num_list.sort()
print(is_num_list_good(num_list, list_size))