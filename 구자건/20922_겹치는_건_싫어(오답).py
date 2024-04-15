from sys import stdin

def find_lcs(sequence, allowed_duplication):
    lcs = 0
    l_pointer = 0
    duplication = dict()
    if sequence == 0:
        return 0
    for r_pointer in range(len(sequence)):
        if not sequence[r_pointer]in duplication.keys():
            duplication[sequence[r_pointer]] = 1
            continue
        if duplication[sequence[r_pointer]] < allowed_duplication:
            duplication[sequence[r_pointer]] += 1
            continue
        lcs = max(lcs, r_pointer - l_pointer)
        while True:
            duplication[sequence[r_pointer]] += 1
            duplication[sequence[l_pointer]] -= 1
            if sequence[l_pointer] == sequence[r_pointer]:
                l_pointer += 1  
                break
            l_pointer += 1 
    return max(lcs, r_pointer - l_pointer + 1)

sequence_size, allowed_duplication = map(int, stdin.readline().split(' '))
sequence = list(map(int, stdin.readline().split(' ')))

print(find_lcs(sequence, allowed_duplication))