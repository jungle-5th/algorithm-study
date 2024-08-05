from sys import stdin
from collections import deque
input = stdin.readline

def spring(food_map, tree_list, dead_list):
    tree_size = len(tree_list)
    for i in range(tree_size):
        tree_age, tree_column, tree_row = tree_list.popleft()
        if tree_age <= food_map[tree_column][tree_row]:
            food_map[tree_column][tree_row] -= tree_age
            tree_list.append([tree_age+1 , tree_column, tree_row])
        else:
            dead_list.append([tree_age, tree_column, tree_row])
    return

def summer(dead_list, food_map):
    while dead_list:
        tree_age, tree_column, tree_row = dead_list.popleft()
        food_map[tree_column][tree_row] += tree_age//2
    return

def fall(tree_list, map_size):
    tree_size = len(tree_list)
    d = [[1, -1],[1, 0], [1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]
    k = 0
    for i in range(tree_size):
        tree_age, tree_column, tree_row = tree_list[i+k]
        if tree_age % 5 == 0:
            for j in range(8):
                dx, dy = d[j]
                y = tree_column + dy
                x = tree_row + dx
                
                if 0 <= x < map_size and 0 <= y < map_size:
                    tree_list.appendleft([1, y, x])
                    k += 1
    return

def winter(feed_map, food_map, map_size):
    for i in range(map_size):
        for j in range(map_size):
            food_map[i][j] += feed_map[i][j]
    return


def tree_investment(map_size, n_tree, target_year):
    food_map = [[5 for i in range(map_size)]for j in range(map_size)]
    feed_map = list()
    tree_list = list()
    dead_list = deque()
    for i in range(map_size):
        feed_map.append(list(map(int, input().split(' '))))
    
    for i in range(n_tree):
        column, row, tree_age = map(int, input().split(' '))
        tree_list.append([tree_age , column-1, row-1])
    tree_list.sort()
    tree_list = deque(tree_list)
    
    for year in range(target_year):
        spring(food_map, tree_list, dead_list)
        summer(dead_list, food_map)
        fall(tree_list, map_size)
        winter(feed_map, food_map, map_size)
        
    return len(tree_list)

map_size, n_tree, target_year = map(int, input().split(' '))
print(tree_investment(map_size, n_tree, target_year))