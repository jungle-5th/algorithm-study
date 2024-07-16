from sys import stdin

input = stdin.readlines

def your_score():
    count = 0
    total_score = 0
    lines = input()
    for line in lines:
        a, score, b = line.rstrip().split(' ')

        if b == 'P':
            continue
        
        score, c= score.split('.')
        score = int(score)

        if b == 'A+':
            total_score += score*4.5
        if b == 'A0':
            total_score += score*4
        if b == 'B+':
            total_score += score*3.5
        if b == 'B0':
            total_score += score*3
        if b == 'C+':
            total_score += score*2.5
        if b == 'C0':
            total_score += score*2
        if b == 'D+':
            total_score += score*1.5
        if b == 'D0':
            total_score += score*1
        count += score

    return total_score/count

print(your_score())
