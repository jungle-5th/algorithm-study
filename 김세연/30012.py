import sys

input = sys.stdin.readline
MAX = sys.maxsize

S, N = map(int, input().split())  # 주인공의 위치 및 개구리의 수

location = [x for x in map(int, input().split())]  # 개구리들의 위치

K, L = map(int, input().split())  # 개구리들의 점프 거리 , 1 걸을 때의 체력 소모량

consumed_hp = {}  # 위치별 체력 소모량 총합


# 개구리가 점프한 거리 대비 체력 소모량 구하기
for i in range(N):
    distance = (
        location[i] - S if location[i] >= S else S - location[i]
    )  # 개구리 간의 거리
    if distance < 2 * K:
        consumed_hp[i] = 2 * K - distance
    else:
        consumed_hp[i] = L * (distance - 2 * K)

# 체력 소모량이 최소인 개구리의 번호와 소모량 찾기
min_no, min_hp = -1, MAX

for i in range(N):
    if min_hp > consumed_hp[i]:
        min_no = i + 1
        min_hp = consumed_hp[i]

print(min_hp, min_no)
