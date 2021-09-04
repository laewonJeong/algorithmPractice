import sys
n,m=map(int,sys.stdin.readline().split())
a=dict(input().split() for _ in range(n))
for i in range(m):
    c=input()
    print(a.get(c))