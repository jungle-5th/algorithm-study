# https://www.acmicpc.net/problem/11387
# 님 무기가 좀 나쁘시네여

cri = list(map(int, input().split(" ")))
pabu = list(map(int, input().split(" ")))
w1 = list(map(int, input().split(" ")))
w2 = list(map(int, input().split(" ")))

cri1 = cri[0] * (1 + cri[1]*0.01) * ((1-min(cri[2]*0.01, 1)) + min(cri[2]*0.01, 1)*cri[3]*0.01)*(1+cri[4]*0.01)
pabu1 = pabu[0] * (1 + pabu[1]*0.01) * ((1-min(pabu[2]*0.01, 1)) + min(pabu[2]*0.01, 1)*pabu[3]*0.01)*(1+pabu[4]*0.01)

for i in range(5):
    cri[i] = cri[i] - w1[i] + w2[i]
    pabu[i] = pabu[i] - w2[i] + w1[i]

cri2 = cri[0] * (1 + cri[1]*0.01) * ((1-min(cri[2]*0.01, 1)) + min(cri[2]*0.01, 1)*cri[3]*0.01)*(1+cri[4]*0.01)
pabu2 = pabu[0] * (1 + pabu[1]*0.01) * ((1-min(pabu[2]*0.01, 1)) + min(pabu[2]*0.01, 1)*pabu[3]*0.01)*(1+pabu[4]*0.01)

if (cri1 > cri2) :  print('-')
elif (cri1 < cri2): print('+')
else: print(0)

if (pabu1 > pabu2): print('-')
elif (pabu1 < pabu2): print('+')
else: print(0)