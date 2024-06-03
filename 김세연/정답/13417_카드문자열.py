# 2024.06.03(월)
# 백준 13417: 카드 문자열 https://www.acmicpc.net/problem/13417
# 주제: 그리디, 문자열, 덱

from sys import stdin
from collections import deque

input = stdin.readline

def sol():
    N = int(input())
    for i in range(N): # 케이스의 갯수
        c_no = int(input()) # 카드 갯수
        input_word = input().strip().split(' ') # 카드 문자열
        foo(c_no, input_word)

def foo(no:int, text:str):
    old_word = [x for x in text] # 받은 카드의 순서
    new_word = deque() # 새로 배치할 카드의 순서
    new_word.append(old_word[0])
    for i in range(1, no): # 아스키코드로 크기 비교후 카드 배치
        new_word.appendleft(old_word[i]) if ord(new_word[0]) - ord(old_word[i]) >= 0 else new_word.append(old_word[i])
    print(''.join(new_word))

sol()