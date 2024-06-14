from sys import stdin
input = stdin.readline

def making_food(sour_list, bitter_list, n_food):
    best_balance = 10**9
    for i in range(1, 2**(n_food)):
        sour = 1
        bitter = 0
        combination = list(format(i, 'b').rjust(n_food, "0"))
        for j in range(n_food):
            if(combination[j] == '1'):
                sour *= sour_list[j]
                bitter += bitter_list[j]
        best_balance = min(best_balance, abs(sour-bitter))
    return best_balance

n_food = int(input())
    
sour_list = list()
bitter_list = list()
for _ in range(n_food):
    sour, bitter = map(int, input().split(' '))
    sour_list.append(sour)
    bitter_list.append(bitter)

print (making_food(sour_list, bitter_list, n_food))