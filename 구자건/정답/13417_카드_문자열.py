from sys import stdin
import string
input = stdin.readline

def card_string():
    n_card = int(input())
    card_list = list(input().rstrip().split(' '))
    
    result = list()
    result.append(card_list[0])
    for i in range(1, n_card):
        if card_list[i] <= result[0]:
            result.insert(0, card_list[i])
        else: result.append(card_list[i])
    result = ''.join(result)
    return result

test_case = int(input())

for _ in range(test_case):
    print(card_string())