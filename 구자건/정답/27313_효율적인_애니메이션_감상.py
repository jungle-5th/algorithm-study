from sys import stdin
def watch_anime():
    global free_time
    ani_pointer = multi_tasking
    time_pointer = 0
    remain_free_time = [free_time - ani_list[i]  for i in range(min(n_ani, multi_tasking))]
    
    for i in range(min(n_ani, multi_tasking)):
        if remain_free_time[i] < 0:
            return i
    ani_count = multi_tasking
    while ani_pointer < n_ani:
        remain_free_time[time_pointer] -= ani_list[ani_pointer]
        if remain_free_time[time_pointer] < 0:
            return ani_count
        ani_count += 1
        ani_pointer += 1
        time_pointer += 1
        if time_pointer >= multi_tasking:
            time_pointer = 0
    
    return ani_count

n_ani, free_time, multi_tasking = map(int, stdin.readline().split(' '))
ani_list = list(map(int, stdin.readline().split(' ')))
ani_list.sort()
print(watch_anime())