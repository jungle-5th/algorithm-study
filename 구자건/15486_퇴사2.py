from sys import stdin

def leave_company():
    severance_pay = dict()
    severance_pay[0] = 0
    
    for remain_day in range(1, remain_days + 1):
        if counseling_table[remain_days - remain_day][0] <= remain_day:
            severance_pay[remain_day] = max(severance_pay[remain_day -1], severance_pay[remain_day - counseling_table[remain_days - remain_day][0]] + counseling_table[remain_days - remain_day][1])
        else:
            severance_pay[remain_day] = severance_pay[remain_day - 1]
    return severance_pay[remain_days]

remain_days = int(stdin.readline())
counseling_table = list()
for _ in range(remain_days):
    days, pay = map(int, stdin.readline().split(' '))
    counseling_table.append([days, pay])

print(leave_company())