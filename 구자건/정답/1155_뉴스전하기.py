from sys import stdin

def news_transfer():
    
    return

people = int(stdin.readline())

sub_tries = [list() for i in range(people)]
company = list(map(int, stdin.readline().split()))

for i in range (1, people):
    if len(sub_tries[people-i]) == 0:
        sub_tries[company[people-i]].append(0)
    else:
        max_time = 0
        n_people = len(sub_tries[people-i])
        sub_tries[people-i].sort()
        for j in range(n_people):
            max_time = max(max_time, sub_tries[people-i][j] + n_people - j)
        sub_tries[company[people-i]].append(max_time)

if len(sub_tries[0]) == 0:
        print(0)
else:
    max_time = 0
    n_people = len(sub_tries[0])
    sub_tries[0].sort()
    for i in range(n_people):
        max_time = max(max_time, sub_tries[0][i] + n_people - i)
    print(max_time)