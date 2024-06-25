from sys import stdin
stdin.readline().split(' ')
list_a = list(map(int, stdin.readline().split(' ')))
list_b = list(map(int, stdin.readline().split(' ')))
list_a = list_a + list_b
list_a.sort()
for i in range(len(list_a)):
    if i == len(list_a)-1:
        print(list_a[i])
    else:print(list_a[i], end = " ")