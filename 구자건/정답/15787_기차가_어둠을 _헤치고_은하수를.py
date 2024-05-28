from sys import stdin
input = stdin.readline

def milky_way(order_set):
    order = order_set
    
    if order[0] == 1:
        train_table[order[1]-1][order[2]-1] = True

    if order[0] == 2:
        train_table[order[1]-1][order[2]-1] = False

    if order[0] == 3:
        train_table[order[1]-1][19] = False
        for i in range(0,19):
            train_table[order[1]-1][19-i] = train_table[order[1]-1][19-i-1]
        train_table[order[1]-1][0] = False

    if order[0] == 4:
        train_table[order[1]-1][0] = False
        for i in range(0,19):
            train_table[order[1]-1][i] = train_table[order[1]-1][i+1]
        train_table[order[1]-1][19] = False

    return

def pass_away():
    count = 0
    for i in range (n_train):
        for j in range (i):
            if train_table[i] == train_table[j]:
                count -= 1
                break
        count += 1
    return count

n_train, n_order = map(int, input().split(' '))
train_table = [[False for _ in range(20)]for __ in range(n_train)]

for i in range(n_order):
    order_set = list(map(int, input().split(' ')))
    milky_way(order_set)

print(pass_away())