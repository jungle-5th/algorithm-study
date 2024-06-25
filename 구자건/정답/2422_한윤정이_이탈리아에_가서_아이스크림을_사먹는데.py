from sys import stdin
input = stdin.readline

def ice_combo(n_ice, n_bad_combo):
    bad_combo_set = set()
    for _ in range(n_bad_combo):
        a, b = map(int, input().split())
        bad_combo_set.add((a, b))

    count = 0
    for i in range(1, n_ice + 1):
        for j in range(i + 1, n_ice + 1):
            if (i, j) in bad_combo_set:
                continue
            for k in range(j + 1, n_ice + 1):
                if (i, k) in bad_combo_set or (j, k) in bad_combo_set:
                    continue
                count += 1
    return count

n_ice, n_bad_combo = map(int, input().split(' '))
print(ice_combo(n_ice, n_bad_combo))