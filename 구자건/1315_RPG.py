from sys import stdin
from collections import deque
input = stdin.readline
def rpg_quest(n_quest):
    max_stat = 1000
    stat_map = [[-1 for _ in range (1001)] for __ in range(1001)]
    stat_map[1][1] = 0
    max_quest = 0
    
    quest_list = list()
    for quest in range(n_quest):
        quest_list.append(list(map(int, input().split(' '))))

    stat_list = deque()
    stat_list.append([1, 1, 0])
    while(stat_list):
        before_s, before_i, before_quest_count = stat_list.popleft()

        for quest_s, quest_i, quest_gain in quest_list:
            if(before_s >= quest_s or before_i >= quest_i) and stat_map[before_s][before_i] == before_quest_count:
                cur_s = min(max_stat, before_s+quest_gain)
                cur_i = min(max_stat, before_i+quest_gain)

                if stat_map[cur_s][cur_i] < before_quest_count + 1:
                    stat_map[cur_s][cur_i] = before_quest_count + 1
                    stat_list.append([cur_s, cur_i, before_quest_count+1])
                    max_quest = max(max_quest, before_quest_count+1)
    print(max_quest)
    return

n_quest = int(input())
rpg_quest(n_quest)