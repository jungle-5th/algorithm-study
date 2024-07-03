from sys import stdin
input = stdin.readline

def difference_group(a, b):
    set_a = set(a)
    set_b = set(b)
    
    set_a = set_a.union(set_b)
    return (len(set_a) - len(b)) + (len(set_a) - len(a))

n_a, n_b = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

print(difference_group(a, b))