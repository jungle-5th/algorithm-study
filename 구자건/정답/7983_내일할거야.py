from sys import stdin

def lazy_girl():
    day = assignment_list[0][1] - assignment_list[0][0]
    for i in range(1, n_assignment):
        if assignment_list[i][1] < day:
            day = assignment_list[i][1] - assignment_list[i][0]
        else: day -= (assignment_list[i][0])
    return day

n_assignment = int(stdin.readline())
assignment_list = list()

for _ in range(n_assignment):
    assignment_list.append(list(map(int, stdin.readline().split(' '))))

assignment_list.sort(key=lambda x:(-x[1], x[0]))

print(lazy_girl())