from sys import stdin

n_green_onion, chicken = map(int, stdin.readline().split())
green_onion_list = list()
min_green_onion = 10*9
max_green_onion = 0
sum_green_onion = 0
for _ in range(n_green_onion):
    green_onion = int(stdin.readline())
    sum_green_onion += green_onion
    min_green_onion = min(min_green_onion, green_onion)
    green_onion_list.append(green_onion)
lp = 1
rp = sum_green_onion // chicken
good_condition_green_onion = 0
while lp <= rp:
    can_make_padak = 0
    seek_onion_length = (lp + rp) // 2
    for green_onion in green_onion_list:
        can_make_padak += green_onion // seek_onion_length
    if can_make_padak < chicken:
        rp = seek_onion_length - 1
    else:
        good_condition_green_onion = max(good_condition_green_onion, seek_onion_length)
        lp = seek_onion_length + 1

print(sum_green_onion - (good_condition_green_onion * chicken))