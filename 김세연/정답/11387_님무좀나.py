# 2024.06.04(화)
# 문제: https://www.acmicpc.net/problem/11387
# 주제: 구현

from sys import stdin

input = stdin.readline

# 솔루션
def sol():
    # 입력받기
    cree = [x for x in map(int, input().split())]
    pabu = [x for x in map(int, input().split())]
    c_weapon = [x for x in map(int, input().split())]
    p_weapon = [x for x in map(int, input().split())]
    # 계산
    print(signs(vs_stat(cree, p_weapon, c_weapon)))
    print(signs(vs_stat(pabu, c_weapon, p_weapon)))

# 스탯 계산
def cp(stat):
    attack, strength, critical_stat, critical_damage, agility = stat
    combat = (
        attack
        * (1 + strength / 100)
        * (
            (1 - min(critical_stat / 100, 1))
            + min(critical_stat / 100, 1) * critical_damage / 100
        )
        * (1 + agility / 100)
    )
    return combat

# 스탯 비교
def vs_stat(player, after_weapon, before_weapon):
    before_stat = cp(player)
    temp = [0] * 5
    for i in range(5):
        temp[i] = player[i] - before_weapon[i] + after_weapon[i]
    after_stat = cp(temp)
    return after_stat - before_stat

# 부호 판단
def signs(number):
    if number > 0:
        return "+"
    elif number < 0:
        return "-"
    else:
        return "0"


sol()
