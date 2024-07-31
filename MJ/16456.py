hawaii = int(input())
if hawaii < 2: print(1); exit()
elif hawaii == 3: print(2); exit()
hawawa = [0, 1, 1, 2]
for i in range(4,hawaii+1): hawawa.append((hawawa[i-1]+hawawa[i-3])%1000000009)
print(hawawa[hawaii])