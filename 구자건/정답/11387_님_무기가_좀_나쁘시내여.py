from sys import stdin
input = stdin.readline

def dps(stat):
    pow = stat[0]*100
    str = stat[1]*100
    crit_rate = stat[2]
    crit_dmg = stat[3]
    speed = stat[4]
    
    dps = pow * (100+(str/100)) * (100*(100-min(100, crit_rate)) + (min(crit_rate, 100)*crit_dmg)) * (100 + speed)
    print(dps)
    return dps

user1_armed_stat = list(map(int, input().split(' ')))
user2_armed_stat = list(map(int, input().split(' ')))
user1_armor = list(map(int, input().split(' ')))
user2_armor = list(map(int, input().split(' ')))

user1_original_dps = dps(user1_armed_stat)
user2_original_dps = dps(user2_armed_stat)

for i in range(5):
    user1_armed_stat[i] -= user1_armor[i]
    user1_armed_stat[i] += user2_armor[i]

for i in range(5):
    user2_armed_stat[i] -= user2_armor[i]
    user2_armed_stat[i] += user1_armor[i]

user1_changed_dps = dps(user1_armed_stat)
user2_changed_dps = dps(user2_armed_stat)

if user1_changed_dps < user1_original_dps:
    print("-")
elif user1_changed_dps > user1_original_dps:
    print("+")
else: print("0")

if user2_changed_dps < user2_original_dps:
    print("-")
elif user2_changed_dps > user2_original_dps:
    print("+")
else: print("0")