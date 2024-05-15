from sys import stdin
def sashimi_jeon_susi(conveyor):
    max_case_size = 0
    case_size = 0
    for i in range(n_dish):
        coupon_valid = True
        case_size = n_sequence + 1
        for j in range(i, i + n_sequence):
            if conveyor[j] in conveyor[j+1: i + n_sequence]:
                case_size -= 1
            if conveyor[j] == coupon:
                coupon_valid = False
            if case_size < max_case_size:
                continue
        if coupon_valid == False:
            case_size -= 1
        if case_size > max_case_size:
            max_case_size = case_size
        if max_case_size == n_sequence + 1:
            return max_case_size

    return max_case_size

n_dish, n_menu, n_sequence, coupon = map(int, stdin.readline().split(' '))
conveyor = list()

for n in range(n_dish):
    susi = int(stdin.readline())
    conveyor.append(susi)

conveyor = conveyor + conveyor[0:n_sequence]

print(sashimi_jeon_susi(conveyor))