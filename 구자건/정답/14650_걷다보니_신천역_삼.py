from sys import stdin
def chanel_number_3(digit):
    count = 0
    for number in range(3**(digit-1), (3**digit)):
        judge = 0
        while number > 0:
            number, mod = divmod(number, 3)
            judge += mod
        
        if judge%3 == 0:
            count+=1
    return count

digit = int(stdin.readline())
print(chanel_number_3(digit))