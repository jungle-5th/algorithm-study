from sys import stdin
def muscle_lose(gain, day):
    global routine_list
    global checked_routine
    day
    cur_gain = gain
    count = 0
    if day == routine:
        if 0 <= gain:
            return 1
        else: return 0
    
    for i in range(routine):
        if checked_routine[i] == False:
            temp = cur_gain
            temp_list = checked_routine.copy()
            cur_gain += routine_list[i]
            if 0 <= cur_gain:
                checked_routine[i] = True
                count += muscle_lose(cur_gain, day + 1)
            cur_gain = temp
            checked_routine = temp_list.copy()
    return count

routine, lose_per_day = map(int, stdin.readline().split(' '))
routine_list = list(map(int, stdin.readline().split(' ')))
checked_routine = [False for _ in range(routine)]
for _ in range(routine):
    routine_list[_] -= lose_per_day
print(muscle_lose(0, 0))