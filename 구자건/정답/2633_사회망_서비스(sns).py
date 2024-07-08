import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def sns(visited_list, node):
    if (len(dp_list[node])) == 0:
        return (0, False)
    
    count = 0
    flag = True
    for i in dp_list[node]:
        if visited_list[i] == False:
            visited_list[i] = True
            sub_link, condition = sns(visited_list, i)
            count += sub_link
            if condition == False:
                flag = False
    if flag == False:
        count += 1
        return (count, True)
    return (count, False)
n_people = int(input())

dp_list = [list() for i in range(n_people + 1)]

for i in range(n_people-1):
    parent, child = map(int, input().split(' '))
    dp_list[parent].append(child)
    dp_list[child].append(parent)
    
visited_list = [False for _ in range(n_people+1)]
visited_list[1] = True
result, plus = sns(visited_list, 1)
print(result)