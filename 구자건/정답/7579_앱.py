from sys import stdin
input = stdin.readline

def application(n_app, need_memory):
    app_list = list(map(int, input().split()))
    cost_list = list(map(int, input().split()))
    
    max_cost = sum(cost_list)
    dp_table = [0] * (max_cost + 1)
    
    for i in range(n_app):
        memory = app_list[i]
        cost = cost_list[i]
        for j in range(max_cost, cost - 1, -1):
            dp_table[j] = max(dp_table[j], dp_table[j - cost] + memory)
    
    for cost in range(max_cost + 1):
        if dp_table[cost] >= need_memory:
            return cost

    return 0

n_app, need_memory = map(int, input().split())

print(application(n_app, need_memory))
