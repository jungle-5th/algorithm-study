from sys import stdin

def maple_story(nova, origin):
    nova_count = 0
    nova_immunity = 0
    nova_cool_time = 0
    
    origin_count = 0
    origin_immunity = 0
    origin_cool_time = 0
    
    nova_list = list(map(int, stdin.readline().split(' ')))
    origin_list = list(map(int, stdin.readline().split(' ')))
    nova_list.sort()
    origin_list.sort()
    
    for i in range(nova):
        if nova_cool_time <= nova_list[i]:
            nova_cool_time = nova_list[i] + 100
            nova_count += 1
    for i in range(origin):
        if origin_cool_time <= origin_list[i]:
            origin_cool_time = origin_list[i] + 360
            origin_count += 1
    print(nova_count, origin_count)
    return

nova, origin = map(int, stdin.readline().split(" "))
maple_story(nova, origin)
