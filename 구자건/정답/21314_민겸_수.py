from sys import stdin

def find_min_min_num():
    min_len = len(min_kyum)
    min_min_value = str()
    
    i = 0
    while i < min_len:
        if min_kyum[min_len - 1 - i] == 'K':
            min_min_value = '5' + min_min_value
        else:
            x=0
            while 0 < min_len - 1 - i:
                if min_kyum[min_len - 2 - i] == 'K':
                    break
                i += 1
                x += 1
            min_min_value = str(10**x) + min_min_value
        i += 1
    return min_min_value

def find_max_min_num():
    min_len = len(min_kyum)
    max_min_value = str()
    
    i = 0
    if min_kyum[min_len - 1 - i] == 'M':
        while 0 < min_len - 1 - i:
            if min_kyum[min_len - 2 - i] == 'K':
                break
            i += 1
            max_min_value = str(1) + max_min_value
    while i < min_len:
        if min_kyum[min_len - 1 - i] == 'K':
            x = 0
            y = 5
            while 0 < min_len - 1 - i:
                if min_kyum[min_len - 2 - i] == 'K':
                    break
                i += 1
                x += 1
            max_min_value = str(y*(10**x)) + max_min_value
        else:
            x=0
            while 0 < min_len - 1 - i:
                if min_kyum[min_len - 2 - i] == 'K':
                    break
                i += 1
                x += 1
            max_min_value = str(10**x) + max_min_value
        i += 1
    return max_min_value

min_kyum = stdin.readline().rstrip()
print(find_max_min_num())
print(find_min_min_num())