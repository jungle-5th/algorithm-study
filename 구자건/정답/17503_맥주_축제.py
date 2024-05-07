from sys import stdin
from heapq import heappop,heappush
def beer_festival():
    drink_list = list()
    satisfaction = 0
    j = 0
    while len(drink_list) < days and j < len(beer[alcohol_type[0]]):
        heappush(drink_list, beer[alcohol_type[0]][j])
        satisfaction += beer[alcohol_type[0]][j]
        j += 1
    if  days <= len(drink_list) and target_satisfaction <= satisfaction:
            return alcohol_type[0]

    for i in range(1, n_alcohol_type):
        for j in range(len(beer[alcohol_type[i]])):
            if len(drink_list) < days:
                heappush(drink_list, beer[alcohol_type[i]][j])
                satisfaction += beer[alcohol_type[i]][j]
            elif drink_list[0] < beer[alcohol_type[i]][j]:
                satisfaction -= heappop(drink_list)
                heappush(drink_list, beer[alcohol_type[i]][j])
                satisfaction += beer[alcohol_type[i]][j]
            else: continue
        if  days <= len(drink_list) and target_satisfaction <= satisfaction:
            return alcohol_type[i]

    return -1

days, target_satisfaction, bear_type = map(int, stdin.readline().split(' '))

beer = dict()
alcohol = dict()
alcohol_type = list()

for _ in range(bear_type):
    satisfaction, alcohol_content = map(int, stdin.readline().split(' '))
    if alcohol_content in alcohol.keys():
        beer[alcohol_content].append(satisfaction)
        alcohol[alcohol_content] += 1
    else:
        beer[alcohol_content] = [satisfaction]
        alcohol[alcohol_content] = 1
        alcohol_type.append(alcohol_content)
        
alcohol_type.sort()
n_alcohol_type = len(alcohol_type)
for i in range(n_alcohol_type):
    beer[alcohol_type[i]].sort(reverse=True)
print(beer_festival())