from sys import stdin

def binary_find(binaryDigits, available_count, order_of_number):
    count = 1
    pointers = [0 for _ in range(binaryDigits)]
    while count < order_of_number:
        pointer = 0
        while(True):
            if pointers[pointer] == 0:
                pointers[pointer] = 1
                for i in range(pointer):
                    pointers[i] = 0
                break
            pointer += 1
        if sum(pointers) <= available_count:
            count += 1
    for i in range(binaryDigits):
        print(pointers[binaryDigits-1-i], end='')
    print()
    return

binaryDigits, available_count, order_of_number = map(int, stdin.readline().split(' '))
binary_find(binaryDigits, available_count, order_of_number)