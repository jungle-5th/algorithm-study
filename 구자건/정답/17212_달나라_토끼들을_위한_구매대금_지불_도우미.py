from sys import stdin
input = stdin.readline

def rabbit_pay(charge):
    n_coin = 4
    coin_list = [0, 1, 2, 5, 7]
    
    coin_pay_table = [[ 0 for i in range(charge+1)] for j in range(n_coin+1)]
    for i in range(len(coin_list)):
        coin_pay_table[i][0] = 0
    for i in range(charge+1):
        coin_pay_table[0][i] = 10**9
    for coins in range(1, n_coin+1):
        for pay in range(1,charge+1):
            for coin in range(1,coins+1):
                coin_value = coin_list[coin]
                if 0 <= pay-coin_value:
                    coin_pay_table[coin][pay] = min(coin_pay_table[coin-1][pay], coin_pay_table[coin][pay-coin_value] + 1)
                else: coin_pay_table[coin][pay] = coin_pay_table[coin-1][pay]
    
    return coin_pay_table[n_coin][charge]

charge = int(input())
print(rabbit_pay(charge))