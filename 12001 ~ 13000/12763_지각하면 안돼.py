import sys

def dfs(graph, cur,time1,money1):
    if cur == n:
        return True
    result = False
    for i,j,k in graph[cur]:
        next = i
        nTime = time1 + j
        nMoney = money1 + k
        if nTime>time or nMoney>money:
            continue
        result = dfs(graph,next,nTime,nMoney)
        if result == True:
            if dist[next][1] > nMoney:
                dist[next][1] = nMoney
    return result
n = int(sys.stdin.readline())
time, money = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
dist=[]
res = float('inf')
for i in range(n+1):
    if i ==1:
        dist.append([0,0])
    else:
        dist.append([float('inf'),float('inf')])
graph=[[] for i in range(n+1)]
for _ in range(m):
    s,d,t,m = map(int,sys.stdin.readline().split())
    graph[s].append([d,t,m])
    graph[d].append([s,t,m])
dfs(graph,1,0,0)
if dist[n][1] == float('inf'):
    print(-1)
else:
    print(dist[n][1])
