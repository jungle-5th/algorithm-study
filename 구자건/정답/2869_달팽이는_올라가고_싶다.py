from sys import stdin

num1, num2, num3 = map(int, stdin.readline().split(' '))

climbing = num1 - num2
first_condition = num3 - num1

if first_condition % climbing == 0:
    print(first_condition // climbing + 1)
else: print(first_condition // climbing + 2)