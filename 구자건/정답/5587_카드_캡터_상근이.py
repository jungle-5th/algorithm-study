from sys import stdin
input = stdin.readline

def sakura(n_card):
    card_list = [False for _ in range(2*n_card)]
    sang_geun = list()
    geun_sang = list()
    for _ in range(n_card):
        card = int(input())
        card_list[card-1] = True
        sang_geun.append(card-1)
        
    for card in range(2*n_card):
        if card_list[card] ==False:
            geun_sang.append(card)
    
    sang_geun.sort(reverse=True)
    geun_sang.sort(reverse=True)
    table = -1
    turn = True
    
    while(sang_geun and geun_sang):
        if turn == True:
            sang_geun_card = len(sang_geun)
            for i in range(sang_geun_card):
                if sang_geun[sang_geun_card-i-1] > table:
                    table = sang_geun.pop(sang_geun_card-i-1)
                    turn = False
                    break
                elif i == sang_geun_card-1:
                    table = -1
                    turn = False
                    break
            continue
        if turn == False:
            geun_sang_card = len(geun_sang)
            for i in range(geun_sang_card):
                if geun_sang[geun_sang_card-i-1] > table:
                    table = geun_sang.pop(geun_sang_card-i-1)
                    turn = True
                    break
                elif i == geun_sang_card-1:
                    table = -1
                    turn = True
                    break
    print(len(geun_sang))
    print(len(sang_geun))
    return
n_card = int(input())
sakura(n_card)