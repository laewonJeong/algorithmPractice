import sys
from collections import deque
def B(a,b):
    q = deque()
    q.append([a,1])
    while q:
        n,c = q.popleft()
        if n == b:
            r = c
            return r
        for i in [n*2,n*10+1]:
            if i>b:
                continue
            q.append([i,c+1])
    return -1
a,b = map(int,sys.stdin.readline().split())
c = B(a,b)
print(c)