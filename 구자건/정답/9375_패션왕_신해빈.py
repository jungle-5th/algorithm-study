from sys import stdin
input = stdin.readline
def fashion_king():
    result = 1
    n_costume = int(input())
    classification = dict()
    for _ in range(n_costume):
        item, class_name = input().split(' ')
        if class_name in classification.keys():
            classification[class_name] += 1
        else:
            classification[class_name] = 1
    n_class = classification.keys()
    for i in n_class:
        result = result * (classification[i]+1)

    print(result)
    return

n_case = int(input())

for _ in range (n_case):
    fashion_king()