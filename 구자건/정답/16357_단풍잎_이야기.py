from sys import stdin
input = stdin.readline

n_keys, n_quest, skills_in_quest = map(int, input().split(' '))
quest_table = [list() for _ in range(n_quest)]
skill_list = list()

for _ in range(n_quest):
    request_keys = list(map(int, input().split(' ')))
    quest_table[_] = request_keys

max_quest = 0

for i in range(2**(2*n_keys)):
    count = 0
    binary = list(map(int, list(format(i, 'b'))))
    if sum(binary) == n_keys:
        for quest in quest_table:
            quest_value = 0
            for skill in quest:
                quest_value += 2**(skill-1)
            if (quest_value & i) == quest_value:
                count += 1
        max_quest = max(max_quest, count)

print(max_quest)