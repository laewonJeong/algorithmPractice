import sys
from collections import deque

def bfs(start,end):
    q=deque()
    q.append([start,""])
    check[start] =1
    while q:
        node,d = q.popleft()
        if node == end:
            print(d)
            return
        D = node*2
        D=D%10000
        if check[D] == 0:
            q.append([D,d+'D'])
            check[D]=1
        if node == 0:
            S=9999
        else: S = node-1
        if check[S] ==0:
            q.append([S,d+'S'])
            check[S] =1
        L = int((node % 1000) * 10 + node / 1000)
        if check[L] == 0:
            q.append([L,d+'L'])
            check[L] =1
        R = int((node % 10) * 1000 + node / 10)
        if check[R] == 0:
            q.append([R,d+'R'])
            check[R] = 1
t = int(sys.stdin.readline())
for _ in range(t):
    check = [0 for _ in range(10000)]
    s, e = map(int,sys.stdin.readline().split())
    bfs(s,e)
