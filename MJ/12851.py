# https://www.acmicpc.net/problem/12851
# 숨바꼭질 2

# 문제
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지
# 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 출력
# 첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# 둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.

# 예제 입력 1 
# 5 17
# 예제 출력 1 
# 4
# 2

n, k = map(int, input().split(" "))
if k <= n:
    print(n-k)
    print(1)
    exit()

# visited는 몇번만에 갈수있고, 몇가지 방법이 있는지
visited = [[0,0] for _ in range(k+3)]
willvisit = [k]
count = 0

def checkNmark(target, idx):
    if visited[target][1] == 0:
        visited[target][0] = count
        visited[target][1] += visited[idx][1]
        willvisit.append(target)
    elif visited[target][0] == count:
        visited[target][1] += visited[idx][1]

if n==0: visited[k][0] = 1; n = 1
else: visited[k][0] = 0 
visited[k][1] = 1

while len(willvisit) > 0:
    idx = willvisit.pop(0)
    if idx > k+1: continue

    count = visited[idx][0]+1

    if idx%2 == 0: checkNmark(idx//2, idx)
    checkNmark(idx+1,idx)
    checkNmark(idx-1,idx)

    if visited[n][0] < count and visited[n][1] !=0:
        print(visited[n][0])
        # print(visited[n][1])
        exit()