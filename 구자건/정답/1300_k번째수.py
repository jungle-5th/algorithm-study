from sys import stdin
input = stdin.readline

def k_th_number(matrix_size,k):
    lp = 1
    rp = min(matrix_size**2, 10**9)
    result = 10**9
    while lp <= rp:
        count = 0
        mid = (lp + rp)//2
        for i in range(1, matrix_size + 1):
            count += min(mid//i, matrix_size)
        if k <= count:
            rp = mid - 1
            result = min(result, mid)
        else :
            lp = mid + 1
    return result

matrix_size = int(input())
k = int(input())
print(k_th_number(matrix_size,k))