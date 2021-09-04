import sys
def be(graph,start):
    d = {}
    for i in range(1,n+1):
        d[i] = float('inf')
    d[start] = 0
    for i in range(n):
        for node in graph:
            for neighbour in graph[node]:
                if d[neighbour] > d[node]+graph[node][neighbour]:
                    d[neighbour] = d[node]+graph[node][neighbour]
                    if i==n-1:
                        return -1
    return d
n,m = map(int,sys.stdin.readline().split())
g={}
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    if a not in g:
        g[a] = {}
    if b not in g[a]:
        g[a][b] =c
    elif g[a][b]>c:
        g[a][b] = c
check = be(g,1)
if check == -1:
    print(-1)
else:
    for i in check:
        if i == 1:
            continue
        if check[i] == float('inf'):
            print(-1)
        else:
            print(check[i])
