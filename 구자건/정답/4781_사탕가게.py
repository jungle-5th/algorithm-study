from sys import stdin

def find_highest_calorie(candy_list, candy_types, budget):
    cart = dict()
    for candy in range(candy_types + 1):
        cart[candy] = [0 for _ in range(budget + 1)]
    
    for candy in range(1, candy_types + 1):
        candy_calorie = candy_list[candy][0]
        candy_price = candy_list[candy][1]
        for cur_price in range(budget + 1):
            if(cur_price < candy_price):
                cart[candy][cur_price] = cart[candy-1][cur_price]
                continue
            cart[candy][cur_price] = max(cart[candy-1][cur_price], cart[candy][cur_price - candy_price] + candy_calorie, cart[candy-1][cur_price - candy_price] + candy_calorie)
            
    return cart[candy_types][budget]

while(True):
    candy_types, budget = stdin.readline().split(' ')
    candy_types = int(candy_types)
    budget = int(budget.replace('.', ''))
    if candy_types == 0:
        break
    
    candy_list = list()
    candy_list.append([0,0])
    candy_list.sort()
    
    for _ in range(candy_types):
        candy_calorie, price = stdin.readline().split(' ')
        candy_calorie = int(candy_calorie)
        price = int(price.replace('.', ''))
        candy_list.append([candy_calorie, price])
    
    print(find_highest_calorie(candy_list, candy_types, budget))