import sys

mascot = []
first_damage = 0
for i in range(3):
    c, d = map(int, sys.stdin.readline().split())
    mascot.append((c,d))
    first_damage += mascot[i][1]
boss_hp = int(sys.stdin.readline()) - first_damage

if boss_hp <= 0:
    print(0)
else:
    time = 1
    while True:
        for c, d in mascot:
            if time % c == 0:
                boss_hp -= d

        if boss_hp <= 0:
            print(time)
            break
        else:
            time+=1