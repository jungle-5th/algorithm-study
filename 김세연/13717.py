# 2024.05.15(수)
# 백준 131717: 포켓몬 고
# 주제: 구현
# 문제요약: 1) 포켓몬들의 진화 가능 횟수의 합 2) 진화를 최대로 많이 하는 포켓몬 구하기

import sys

input = sys.stdin.readline


def sol():

    N, pokemon = inputs()
    lv_sum, max_pokemon = logic(N, pokemon)

    # 최대 진화 포켓몬을 위한 max(레벨, 이름) 리스트 만들기
    print(lv_sum)
    print(max_pokemon)


# 포켓몬들을 이름, 진화캔디, 현재캔디 갯수 받기
def inputs() -> tuple:
    N = int(input())
    pokemon = [None] * N

    for i in range(N):
        name = input().strip()
        candy, current = map(int, input().split())
        pokemon[i] = [name, candy, current]

    return (N, pokemon)


# 로직: 진화횟수의 합, 진화를 최대로 많이 하는 포켓몬 구하기
def logic(N: int, pokemon: list) -> tuple:
    lv_sum, lv_max = 0, 0
    max_pokemon = ""
    for i in range(N):
        name, candy, current = pokemon[i]
        lv = 0
        while current // candy > 0: # 현재 갯수로 진화할 수 없을 때까지
            current -= candy - 2    # 캔디 갯수 소모 + 진화마다 2 이득 반영
            lv += 1                 # loop 마다 레벨업
        lv_sum += lv                # 레벨의 합에 레벨 추가
        if lv_max < lv:             # 최대 횟수 진화 갱신
            lv_max = lv
            max_pokemon = name      # 최대진화 포켓몬 갱신
    return (lv_sum, max_pokemon)


sol()
