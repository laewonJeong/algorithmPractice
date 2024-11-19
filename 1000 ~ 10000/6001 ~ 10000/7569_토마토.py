import sys
from collections import deque

check = []
def bfs(graph):
    q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    q.append([j,k,i])
    while q:
        x,y,z = q.popleft()
        for i in range(6):
            if i == 0:
                tx = x-1
                ty =y
                th = z
            elif i ==1:
                tx = x+1
                ty =y
                th = z
            elif i==2:
                ty = y-1
                tx =x
                th = z
            elif i==3:
                ty = y+1
                tx =x
                th = z
            elif i==4:
                ty = y
                tx =x
                th = z+1
            elif i==5:
                ty = y
                tx =x
                th = z-1
            if (0<=tx<n) and (0<=ty<m) and (0<=th<h) and graph[th][tx][ty] == 0:
                graph[th][tx][ty] = graph[z][x][y]+1
                q.append([tx,ty,th])
    return graph

m,n,h = map(int,sys.stdin.readline().split())
check1 = 0
graph=[]
for i in range(h):
    graph.append([])
    for j in range(n):
        graph[i].append(list(map(int,sys.stdin.readline().split())))
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                check1 +=1
arr = bfs(graph)
check = 0
max = -987654321
for i in arr:
    for j in i:
        for k in j:
            if k>max:
                max = k
            if k == 0:
                check =1
                break
if check1 == 0:
    print(0)
elif check == 1:
    print(-1)
else:
    print(max-1)
