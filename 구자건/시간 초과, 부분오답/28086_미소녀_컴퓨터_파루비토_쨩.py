from sys import stdin

def separate_expression(expression):
    global octal_number_a
    global octal_number_b
    global operator
    expression_list = list(expression)
    length = len(expression_list)
    separate_point = 0
    for i in range(length):
        seek_point = length -1 -i
        if expression_list[seek_point] in operators:
            if expression_list[seek_point-1] in operators:
                separate_point = seek_point-1
            else:
                separate_point = seek_point
            break
    octal_number_a = expression_list[0 : separate_point]
    octal_number_b = expression_list[separate_point+1 : length]
    operator = expression_list[separate_point]
    return

def to_decimal(octal_number):
    is_minus = False
    value = 0
    if octal_number[0] == '-':
        is_minus = True
        octal_number.remove('-')
    octal_number.reverse()
    length = len(octal_number)
    
    for i in range (length):
        value += (int(octal_number[i])*(8**i))
    if is_minus == True:
        return -value
    else: return value

def to_octal(number):
    is_minus = False
    octal_number_list = list()
    if number < 0:
        number = number * -1
        is_minus = True
    
    while number > 8:
        insert_number = number % 8
        number = number // 8
        octal_number_list.append(str(insert_number))
    if number!=0:
        octal_number_list.append(str(number))
    
    if is_minus == True:
        octal_number_list.append('-')
    return octal_number_list

octal_number_a = list()
octal_number_b = list()
operator = "k"
operators = ['+', '-', '*', '/']

expression = stdin.readline().rstrip()
separate_expression(expression)
decimal_a = to_decimal(octal_number_a)
decimal_b = to_decimal(octal_number_b)

if decimal_b != 0:
    if operator == '+':
        result = decimal_a + decimal_b
    if operator == '-':
        result = decimal_a - decimal_b
    if operator == '*':
        result = decimal_a * decimal_b
    if operator == '/':
        result = decimal_a // decimal_b
    result = to_octal(result)
    result.reverse()
    print("".join(result))
else: print("invalid")