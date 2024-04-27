num1, num2, num3 = map(int, input().split(' '))
print(((num3 - num1) // (num1 - num2)) + 2) if (num3 - num1) % (num1 - num2) else print(((num3 - num1) // (num1 - num2)) + 1)