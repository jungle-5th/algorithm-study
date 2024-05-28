from sys import stdin
input = stdin.readline

days = int(input())
mood_list = list(map(int, input().split()))

flower_giving = [False for _ in range(days)]
count = 0
depressed_day = dict()

for i in range(days):
    if mood_list[days - i - 1] < 0:
        count += 1
        if mood_list[days - i - 2] >= 0  and 0 <= days - i - 2:
            if count in depressed_day.keys():
                depressed_day[count].append(i)
                count = 0
            else:
                depressed_day[count] = list()
                depressed_day[count].append(days - i - 1)
                count = 0

depressed_day_lengths = list(depressed_day.keys())
depressed_day_lengths.sort()
n_length_key = len(depressed_day_lengths)

count = 0
for i in range(n_length_key-1):
    for day in depressed_day[depressed_day_lengths[i]]:
        for j in range(1, (2*depressed_day_lengths[i])+1):
            if day - j < 0:
                break
            if flower_giving[day - j] == False:
                flower_giving[day - j] = True
                count += 1
max_count = count


length = len(depressed_day[depressed_day_lengths[n_length_key-1]])

for i in range (length):
    temp = count
    temp_list = flower_giving.copy()
    
    for j in range(length):
        day = depressed_day[depressed_day_lengths[n_length_key-1]][j]
        if i == j :
            for k in range(1, (3*depressed_day_lengths[n_length_key-1])+1):
                if day - k < 0:
                    break
                if flower_giving[day - k] == False:
                    flower_giving[day - k] = True
                    count += 1
        else:
            for k in range(1, (2*depressed_day_lengths[n_length_key-1])+1):
                if day - k < 0:
                    break
                if flower_giving[day - k] == False:
                    flower_giving[day - k] = True
                    count += 1
    max_count = max(max_count, count)
    count = temp
    flower_giving = temp_list.copy()

print(max_count)