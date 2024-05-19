from sys import stdin
def group_input():
    group_name = stdin.readline().rstrip()
    group_table[group_name] = list()
    n_member = int(stdin.readline())
    for member in range(n_member):
        member_name = stdin.readline().rstrip()
        member_table[member_name] = group_name
        group_table[group_name].append(member_name)
    group_table[group_name].sort()
    return
n_group, n_quiz = map(int, stdin.readline().split(' '))

group_table = dict()
member_table = dict()

for _ in range(n_group):
    group_input()

for _ in range(n_quiz):
    quiz = stdin.readline().rstrip()
    quiz_type = int(stdin.readline())
    if quiz_type:
        print(member_table[quiz])
    else:
        for i in group_table[quiz]:
            print(i)