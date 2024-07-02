from sys import stdin
input = stdin.readline

def difference_group(a, b):
    set_a = set(a)
    set_b = set(b)
    
    for i in set_b:
        set_a.add(i)
    
    return len(set_a) - len(b)

n_a, n_b = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

n_a_difference_b = difference_group(a, b)
n_b_difference_a = difference_group(b, a)

print(n_a_difference_b + n_b_difference_a)