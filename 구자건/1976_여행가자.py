from sys import stdin

def can_we_go_journey(adj_list, n_city, tour_course, n_journey_spot):
    for pass_city in range(n_city):
        for start in range(n_city):
            for end in range(n_city):
                if adj_list[start][pass_city] != 0 and adj_list[pass_city][end] != 0:
                    adj_list[start][end] = 1
    for city in range(n_journey_spot-1):
        if tour_course[city] == tour_course[city+1]: continue
        if adj_list[tour_course[city]-1][tour_course[city+1]-1] == 0:
            return 'NO'
    return 'YES'

n_city = int(stdin.readline())
n_journey_spot = int(stdin.readline())
adj_list = list()
for city_adj in range(n_city):
    adj_line = list(map(int, stdin.readline().split(' ')))
    adj_list.append(adj_line)
tour_course = list(map(int, stdin.readline().split(' ')))

print(can_we_go_journey(adj_list, n_city, tour_course, n_journey_spot))
