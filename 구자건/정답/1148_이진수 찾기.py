from sys import stdin

def binary_find(binaryDigits, allowed_True_count, order_of_number):
    count_of_combination = dict()
    count_of_combination[0] = [0 for _ in range(allowed_True_count+1)]
    count_of_combination[0][0] = 1
    combination_sum = 1
    before_sum = combination_sum
    digit = 0
    
    while combination_sum < order_of_number:
        digit += 1
        before_sum = combination_sum
        count_of_combination[digit] = list()
        count_of_combination[digit].append(1)
        for true_count in range(1, allowed_True_count+1):
            count_of_combination[digit].append(count_of_combination[digit-1][true_count-1] + count_of_combination[digit-1][true_count])
        combination_sum = sum(count_of_combination[digit])
    
    current_order = before_sum + 1
    digit_pointers = [0 for _ in range(binaryDigits)]
    
    if(0 <= digit-1):
        digit_pointers[digit-1] = 1
    
    pointer = 0
    remain_digit = allowed_True_count - 1
    while current_order < order_of_number:
        if order_of_number >= current_order +sum(count_of_combination[digit - 1 - pointer][0: remain_digit+1]):
            current_order = current_order +sum(count_of_combination[digit - 1 - pointer][0: remain_digit+1])
            digit_pointers[digit - 1 - pointer] = 1
            remain_digit -= 1
        pointer += 1
    digit_pointers.reverse()
    digit_pointers = ''.join(map(str, digit_pointers))
    print(digit_pointers)
    return

binaryDigits, allowed_True_count, order_of_number = map(int, stdin.readline().split(' '))
binary_find(binaryDigits, allowed_True_count, order_of_number)