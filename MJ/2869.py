climb, slip, goal = map(int, input().split(" "))
print(1 if goal == climb else ((goal-climb-1)//(climb-slip) + 2))