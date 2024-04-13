from sys import stdin
from heapq import heappop, heappush

def merge_card_deck(card_decks):
    count = 0
    while(len(card_decks)>1):
        card_deck1 = heappop(card_decks)
        card_deck2 = heappop(card_decks)
        new_card_deck = card_deck1 + card_deck2
        count += new_card_deck
        heappush(card_decks, new_card_deck)
    return count

card_decks = list()
n_card_decks = int(stdin.readline())
for i in range(n_card_decks):
    heappush(card_decks, int(stdin.readline()))
print(merge_card_deck(card_decks))