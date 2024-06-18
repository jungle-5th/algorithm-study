from sys import stdin
input = stdin.readline

def number_counting_sheep(case_number):
    sample = [False for _ in range(10)]
    
    test_number = int(input())
    if(test_number == 0):
        print('Case #{0}: INSOMNIA'.format(case_number))
        return
    i = 0
    while False in sample:
        i += 1
        formatting_number = test_number*i
        while formatting_number > 0:
            labelling_number = formatting_number % 10
            formatting_number = formatting_number // 10
            sample[labelling_number] = True
    
    print('Case #{0}: {1}'.format(case_number, test_number*i))
    return

n_case = int(input())

for i in range(1, n_case+1):
    number_counting_sheep(i)
