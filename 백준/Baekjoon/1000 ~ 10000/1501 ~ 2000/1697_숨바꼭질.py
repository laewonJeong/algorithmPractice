import sys
from collections import deque

check={}
def bfs(start,end):
    check[start] = 0
    q=deque()
    q.append(start)
    while q:
        node = q.popleft()
        if node == end:
            print(check[node])
            return
        for edge in [node-1,node+1,node*2]:
            if 0<=edge<1000001 and edge not in check:
                check[edge] = check[node]+1
                q.append(edge)

n,k = map(int,sys.stdin.readline().split())
bfs(n,k)
