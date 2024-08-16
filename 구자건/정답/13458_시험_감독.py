from sys import stdin
from math import ceil
input = stdin.readline

def director(n_class):
    class_list = list(map(int, input().split(' ')))
    supervisor, sub_supervisor = map(int, input().split(' '))
    count = n_class
    
    for _class in class_list:
        _class -= supervisor
        if 0 < _class:
            count += ceil(_class / sub_supervisor)
    return count

n_class = int(input())
print(director(n_class))