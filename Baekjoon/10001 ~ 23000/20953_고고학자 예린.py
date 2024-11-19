import sys
n = int(sys.stdin.readline())
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    print(((x+y)*(x+y))*(x+y-1)//2)