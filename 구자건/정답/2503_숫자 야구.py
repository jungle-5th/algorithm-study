from sys import stdin
input = stdin.readline

def base_ball(n_quest):
    question_list = list()
    result_list = list()
    test_sample = list()
    
    count = 0
    for _ in range (n_quest):
        question, strike, ball = input().split(' ')
        question_list.append(list(map(int, question)))
        result_list.append([int(strike), int(ball)])
    
    for i in range(100, 1000):
        test_sample = list(map(int,str(i)))
        valid = True
        if 0 in test_sample:
            continue
        for j in range(3):
            for k in range(j+1, 3):
                if test_sample[j] == test_sample[k]:
                    valid = False
        if(valid == False):
            continue
        count_flag = True
        for j in range(n_quest):
            strike, ball = 0, 0
            for k in range(3):
                if test_sample[k] == question_list[j][k]:
                    strike += 1
                    continue
                if test_sample[k] in question_list[j]:
                    ball += 1
            if strike != result_list[j][0] or ball != result_list[j][1]:
                count_flag = False
                break
        if count_flag == True:
            count += 1
    return count

n_quest = int(input())

print(base_ball(n_quest))