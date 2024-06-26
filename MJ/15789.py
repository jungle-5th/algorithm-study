# https://www.acmicpc.net/problem/15789
# CTP 왕국은 한솔 왕국을 이길 수 있을까?

# 문제
# CTP 왕국은 정말 깊은 역사를 가지고 있다. 선대 김진서 왕부터 시작하여 전현용 왕을 거쳐 … 마침내 김세진이 CTP 왕국의 왕이되었다.
# 세진이는 재미없는 개그를 정말 싫어했기 때문에 왕이 되자마자 CTP 왕국에서 가장 재미없는 이한솔을 쫓아냈다. 
# 화가난 한솔이는 자기의 개그에 유일하게 웃어주던 박정률과 함께 한솔 왕국을 세웠다.
# 그 이후 33년이 지났다 …………. 
# 어느새 한솔 왕국은 번창하여 CTP 왕국보다 힘이 쎄졌다. 세진이는 다른 왕국과 동맹을 맺어 CTP 왕국의 힘을 길러 한솔 왕국보다 부흥시키려고 한다.
# 왕국의 힘이란 동맹국의 수를 의미한다.  (예를 들어 동맹이 없는 나라의 힘은 1이다)
# 왕국간의 동맹의 법칙은 조금 특별해서 만약에 A왕국과 B왕국이 동맹이고 B왕국과 C왕국이 동맹이라면 A왕국과 C왕국도 동맹이 된다. 
# CTP 왕국의 왕 세진이는 최대 K번 다른 왕국과 동맹을 맺을 기회를 갖으며, 현재 동맹관계는 CTP 왕국과 한솔 왕국은 동맹이 아니다.
# 또한 한솔 왕국과 동맹인 왕국과는 동맹을 맺을 수 없으며 K번의 동맹 맺을 기회를 모두 사용하지 않아도 된다.
# 각 왕국들의 동맹관계와 CTP 왕국의 번호, 한솔 왕국의 번호가 주어질 때 세진이를 도와 CTP 왕국의 힘의 최댓값을 구하여라.
# 각 왕국의 번호는 1부터 N까지의 자연수로 나타내어지며, 서로 다른 두 왕국이 같은 번호를 갖는 경우는 없다.

# 입력
# 입력의 첫째 줄에 왕국의 수 N(3 ≤ N ≤ 100,000)과 동맹 관계의 수 M(1 ≤ M ≤ 200,000)이 주어진다.
# 이 후 M개의 줄에 X,Y가 주어진다. 이는 X 왕국과 Y 왕국이 동맹이라는 뜻이다.
# 입력의 마지막 줄에 CTP 왕국의 번호 C와 한솔 왕국의 번호 H와 추가 동맹의 기회 K(0 ≤ K ≤ 100)가 공백으로 구분되어 주어진다. 
# 주어지는 입력에서 CTP 왕국과 한솔 왕국은 절대로 동맹이 되지 않게 주어진다.

# 출력
# CTP 왕국의 힘의 최댓값을 출력하라. 

# 예제 입력 1 
# 10 7
# 1 2
# 1 3
# 2 3
# 1 4
# 5 6
# 8 10
# 7 9
# 5 9 1
# 예제 출력 1 
# 6

import sys
import queue

n_of_nations, e_of_edges = map(int, sys.stdin.readline().split(" "))
flags = [-1 for n in range(n_of_nations+1)]
flags[0] = 0
def find_union(a) :
    if flags[a] < 0: return a
    flags[a] = find_union(flags[a])
    return flags[a]
    
for _ in range(e_of_edges):
    a, b = map(int, sys.stdin.readline().split(" "))
    if a > b: a, b = b, a
    ruler_a = find_union(a)
    ruler_b = find_union(b)
    if(ruler_a == ruler_b) : continue
    flags[ruler_a] += flags[ruler_b]
    flags[ruler_b] = ruler_a

sejin, hansol, chance = map(int, sys.stdin.readline().split(" "))
power = -flags[find_union(sejin)]
flags[find_union(hansol)] = 0

kings = []
for i in range(n_of_nations+1):
    if flags[i] < 0: kings.append(flags[i])
kings = sorted(kings)
for c in range(chance):
    if(len(kings) == 0): break
    power -= kings[c]

print(power)