from sys import stdin

def sudden_attack_3(n_player):
    if n_player == 1:
        print('Yes')
        return
    player_list = list(map(int, stdin.readline().split(' ')))
    joonwon = player_list.pop(0)
    
    player_list.sort()
    
    for i in range(len(player_list)):
        if(joonwon <= player_list[i]):
            print('No')
            return
        joonwon += player_list[i]
    
    print('Yes')
    return

n_player = int(stdin.readline())
sudden_attack_3(n_player)