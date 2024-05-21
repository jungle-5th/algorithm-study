# 2024.05.10(금)
# 백준 16165: 걸그룹 마스터 준석이

import sys

input = sys.stdin.readline

group_total, quiz_total = map(int, input().split())

groups = {}
members = {}

# 걸그룹 입력 받기
for i in range(group_total):
    group_name = input().strip()
    member_total = int(input())
    group_member = [None] * member_total
    for i in range(member_total):
        member = input().strip()
        group_member[i] = member  # 그룹에 멤버 추가
        members[member] = group_name  # 멤버-그룹 해시맵 만들기
    group_member.sort()  # 이름순으로 정렬
    groups[group_name] = (
        tuple(group_member)  # 사전에 그룹을 키로 그룹멤버 리스트를 값으로 넣기
    )

# 퀴즈 구현

def solve_quiz(quiz, quiz_type):
    if quiz_type == 1:
        find_group = members[quiz]
        print(find_group)
    elif quiz_type == 0:
        group = groups[quiz]
        for member in group:
            print(member)


for i in range(quiz_total):
    quiz = input().strip()
    quiz_type = int(input())
    solve_quiz(quiz, quiz_type)
