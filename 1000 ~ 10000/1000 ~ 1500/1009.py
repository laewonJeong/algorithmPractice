import sys
num = int(input())
for _ in range(num):
    n,m = map(int,sys.stdin.readline().split())
    if pow(n,m,10) == 0:
        print(10)
    else:
        print(pow(n,m,10))