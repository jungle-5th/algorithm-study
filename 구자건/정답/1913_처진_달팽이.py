from sys import stdin
def snail(number, finding_number):
    finding_column = 0
    finding_row = 0
    snail = [[0 for _ in range(number)] for __ in range(number)]
    phase_1_limit = number - 1
    phase_2_limit = number - 1
    phase_3_limit = 0
    phase_4_limit = 1
    n = number**2
    phase = 1
    column, row = -1, 0
    while 0 < n:
        if phase == 1:
            while column < phase_1_limit:
                column += 1
                snail[column][row] = n
                n -= 1
            phase_1_limit -= 1
            phase = 2
        elif phase == 2:
            while row < phase_2_limit:
                row += 1
                snail[column][row] = n
                n -= 1
            phase_2_limit -= 1
            phase = 3
        elif phase == 3:
            while column > phase_3_limit:
                column -= 1
                snail[column][row] = n
                n -= 1
            phase_3_limit += 1
            phase = 4
        elif phase == 4:
            while row > phase_4_limit:
                row -= 1
                snail[column][row] = n
                n -= 1
            phase_4_limit += 1
            phase = 1
    for i in range(number):
        line = snail[i]
        for j in range(number):
            print(line[j], end=' ')
            if line[j] == finding_number:
                finding_column = i + 1
                finding_row = j + 1
        print()
    print(f"{finding_column} {finding_row}" )
    return

number = int(stdin.readline())
finding_number = int(stdin.readline())

snail(number, finding_number)