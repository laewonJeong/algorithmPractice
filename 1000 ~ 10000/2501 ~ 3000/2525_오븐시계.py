import sys
hour,min = map(int,sys.stdin.readline().split())
plus_min = int(sys.stdin.readline())
for i in range(plus_min):
    min += 1
    if min >=60:
        min -= 60
        hour+=1
        if hour>=24:
            hour-=24
print(f'{hour} {min}')