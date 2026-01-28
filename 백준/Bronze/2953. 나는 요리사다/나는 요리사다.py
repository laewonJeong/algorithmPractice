import sys
max = 0
for i in range(1,6):
    a,b,c,d = map(int,sys.stdin.readline().split())
    if a+b+c+d > max:
        max = a+b+c+d
        ans = i
print(f'{ans} {max}')