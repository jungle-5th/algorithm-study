from sys import stdin
from math import sqrt
def factorization(num):
    if num == 1:
        return
    
    number = num
    factor = 2
    while factor*factor <= num:
        if number % factor == 0:
            print(factor)
            number = number // factor
            continue
        factor += 1
    
    if number > 1 : print(number)
    return

num = int(stdin.readline())
factorization(num)