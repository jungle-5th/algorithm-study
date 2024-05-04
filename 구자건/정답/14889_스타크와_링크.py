from sys import stdin

from sys import stdin

def team_mating(people):
    min_different = 10**9
    a_team_stat = 0
    b_team_stat = 0
    team_value = people//2
    for combination in range(2**(people-1), 2**people):
        a_team_stat = 0
        b_team_stat = 0
        a_list = list()
        b_list = list()
        team = list(map(int, list(format(combination, 'b'))))
        if sum(team) == team_value:
            for i in range(people):
                if team[i] == 1:
                    for a_team_people in a_list:
                        a_team_stat += stat_map[a_team_people][i]
                    a_list.append(i)
                if team[i] == 0:
                    for b_team_people in b_list:
                        b_team_stat += stat_map[b_team_people][i]
                    b_list.append(i)
            if abs(b_team_stat - a_team_stat) < min_different:
                min_different = abs(b_team_stat - a_team_stat)
    return min_different

stat_map = list()
people = int(stdin.readline())
for _ in range(people):
    stat_map.append(list(map(int, stdin.readline().split(' '))))
    for __ in range(_):
        stat_map[__][_] += stat_map[_][__]

print(team_mating(people))