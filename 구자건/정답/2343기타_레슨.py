from sys import stdin
def guitar_lesson(lessons, n_blue_ray):
    total_lesson_time = sum(lessons)
    lp = max(lessons)
    rp = total_lesson_time
    min_blue_ray = 2147483647
    
    while lp <= rp:
        seek_pointer = (lp+rp)//2
        blue_ray_to_make = 1
        burn = 0
        for lesson in lessons:
            burn += lesson
            if seek_pointer < burn:
                blue_ray_to_make += 1
                burn = lesson
        
        if blue_ray_to_make <= n_blue_ray:
            rp = seek_pointer-1
            min_blue_ray = min(min_blue_ray, seek_pointer)
        else:
            lp = seek_pointer+1
    return min_blue_ray

n_lesson, n_blue_ray = map(int, stdin.readline().split(' '))
lessons = list(map(int, stdin.readline().split(' ')))

print(guitar_lesson(lessons, n_blue_ray))