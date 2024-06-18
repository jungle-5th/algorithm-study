from sys import stdin

def trans_x_to_decimal(number):
    num_length = len(number) - 2
    index = len(number)-1
    value = 0
    
    for i in range(0, num_length):
        if number[index -i] == "f":
            value += 15 * (16**(i))
            continue
        if number[index -i] == "e":
            value += 14 * (16**(i))
            continue
        if number[index -i] == "d":
            value += 13 * (16**(i))
            continue
        if number[index -i] == "c":
            value += 12 * (16**(i))
            continue
        if number[index -i] == "b":
            value += 11 * (16**(i))
            continue
        if number[index -i] == "a":
            value += 10 * (16**(i))
            continue
        value += int(number[index -i]) * (16**(i))
    print(value)
    return

def trans_o_to_decimal(number):
    num_length = len(number) - 1
    index = len(number)-1
    value = 0
    
    for i in range(0, num_length):
        value += int(number[index -i]) * (8**(i))
    print(value)
    return

num = stdin.readline()
number = list(num.rstrip())

if number == "0":
    print(number)
elif number[0] != "0": print(num)
elif number[1] == "x":
    trans_x_to_decimal(number)
else: trans_o_to_decimal(number)