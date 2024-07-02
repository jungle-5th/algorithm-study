from sys import stdin
from collections import deque
input = stdin.readline
def rpg_quest(n_quest):
    stat_map = [[0 for _ in range (1001)] for __ in range(1001)]
    stat_map[1][1] = 0
    max_quest = 0
    
    quest_list = list()
    for quest in range(n_quest):
        quest_list.append(list(map(int, input().split(' '))))
    get_stat = 0
    
    for quest in quest_list:
        if quest[0] <= 1 or quest[1] <= 1:
            stat_map[1][1] += 1
            get_stat += quest[2]
    
    stat_list = deque()

    stat_list.append([1, 1, get_stat, stat_map[1][1]])
    max_quest = max(max_quest, stat_map[1][1])
    while(stat_list):
        before_s, before_i, before_get_stat, before_quest_count = stat_list.popleft()
        for i in range(before_get_stat+1):
            quest_count = before_quest_count
            get_stat = 0
            cur_s = before_s + i
            cur_i = before_s + before_get_stat - i
            
            if cur_s >= 1000 or cur_i >= 1000:
                print(n_quest)
                return
            
            for quest in quest_list:
                if (before_s < quest[0] and before_i < quest[1]) and (quest[0] <= cur_s or quest[1] <= cur_i):
                    get_stat += quest[2]
                    quest_count += 1
            if(get_stat != 0):
                stat_map[cur_s][cur_i] = max(quest_count, stat_map[cur_s][cur_i])
                max_quest = max(max_quest, quest_count)
                stat_list.append([cur_s, cur_i, get_stat, quest_count])
    print(max_quest)
    return

n_quest = int(input())
rpg_quest(n_quest)