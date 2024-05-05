from sys import stdin
from heapq import heappush, heappop
def classroom_schedule():
    class_number = 1
    heappush(class_room, [lesson[0][2],class_number])
    class_match[lesson[0][0]-1] = class_number
    
    for i in range(1, n_lesson):
        if class_room[0][0] > lesson[i][1]:
            class_number +=1
            class_match[lesson[i][0]-1] = class_number
            heappush(class_room, [lesson[i][2], class_number])
        else:
            temp = heappop(class_room)
            class_match[lesson[i][0]-1] = temp[1]
            heappush(class_room, [lesson[i][2], temp[1]])
    return

n_lesson = int(stdin.readline())
class_match = [0 for _ in range(n_lesson)]
class_room = list()
lesson = [list(map(int, stdin.readline().split(' '))) for i in range(n_lesson)]
lesson.sort(key=lambda x:(x[1], x[2]))

classroom_schedule()
print(len(class_room))
for room in class_match:
    print(room)