n_of_drinks = int(input())
result, maxval = 0, 0
drink = list(map(float, input().split(" ")))
for i in range(n_of_drinks):
    result += drink[i]/2
    if drink[i]/2 > maxval: maxval = drink[i]/2
print(result+maxval)