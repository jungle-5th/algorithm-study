from sys import stdin
input = stdin.readline

def rabbit_pay(charge, n_coin):
    coin_list = [0]
    for i in range(n_coin):
        coin_list.append(int(input()))
    
    coin_pay_table = [ 0 for i in range(charge+1)]
    coin_pay_table[0] = 1
    for coin in range(1,n_coin+1):
        for pay in range(1,charge+1):
            coin_value = coin_list[coin]
            if 0 <= pay-coin_value:
                coin_pay_table[pay] = coin_pay_table[pay] + coin_pay_table[pay-coin_value]
    
    return coin_pay_table[charge]

n_coin, charge = map(int, input().split(' '))
print(rabbit_pay(charge, n_coin))