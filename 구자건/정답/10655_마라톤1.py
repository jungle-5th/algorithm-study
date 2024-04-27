from sys import stdin
def marathon():
    check_point
    return
n_point = int(stdin.readline())
check_points = [[0, 0] for _ in range(n_point)]
max_cut = 0
course_range = [ 0 for _ in range(n_point)]

first_x, first_y = map(int, stdin.readline().split(' '))
check_points[0] = [first_x, first_y]

x, y = map(int, stdin.readline().split(' '))
check_points[1] = [x, y]
course_range[1] = (abs(check_points[0][0] - x) + abs(check_points[0][1] - y))

for check_point in range(2, n_point):
    x, y = map(int, stdin.readline().split(' '))
    check_points[check_point] = [x, y]
    course_range[check_point] = (abs(check_points[check_point-1][0] - x) + abs(check_points[check_point-1][1] - y))
    short_cut_range = course_range[check_point] + course_range[check_point-1] - (abs(check_points[check_point-2][0] - x) + abs(check_points[check_point-2][1] - y))
    max_cut = max(max_cut, short_cut_range)

print(sum(course_range) - max_cut)