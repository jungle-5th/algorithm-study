import sys
nova_and_ori = list(map(int, sys.stdin.readline().split(" ")))
nova = sorted(list(map(int, sys.stdin.readline().split(" "))))
ori = sorted(list(map(int, sys.stdin.readline().split(" "))))
novacnt, oricnt, novacool, oricool = 0,0,0,0
for n in nova:
    if n >= novacool:
        novacool = n+100
        novacnt += 1
for o in ori:
    if o >= oricool:
        oricool = o+360
        oricnt += 1
print(novacnt, oricnt)
