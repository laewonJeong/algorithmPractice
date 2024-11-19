import sys
ans = 1
a=int(sys.stdin.readline())
list = [[0 for col in range(2)] for row in range(a)]
for i in range(a):
    b,c = map(int,sys.stdin.readline().split())
    list[i][0] = b
    list[i][1] = c
list = sorted(list)
for i in range(a):
    print(f'{list[i][0]} {list[i][1]}')