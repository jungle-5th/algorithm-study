k, n = map(int,input().split(" "))
sum = 0
max = 0
cables = [0] * k
for i in range(k):
    c = int(input())
    cables[i] = c
    sum += c
    if (c > max): max = c

# sort(cables.begin(), cables.end(), greater<>())

ref = sum//n
lo = 1
hi = max
if ref==0: ref = 1
while True :
    res = 0
    for i in range(k) :
        res += cables[i]//ref 

    if (res < n) :
        hi = ref
        ref = (lo+ref)//2
    else :
        lo = ref
        ref = (hi+ref)//2
    
    if (ref == lo) :print(ref); exit()