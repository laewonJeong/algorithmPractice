import sys
from collections import deque

check = []
def bfs(graph):
    q = deque()
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
               q.append([i,j])
    while q:
        x,y = q.popleft()
        for i in range(4):
            if i == 0:
                tx = x-1
                ty =y
            elif i ==1:
                tx = x+1
                ty =y
            elif i==2:
                ty = y-1
                tx =x
            elif i==3:
                ty = y+1
                tx =x
            if (0<=tx<m) and (0<=ty<n) and graph[tx][ty] == 0:
                graph[tx][ty] = graph[x][y]+1
                q.append([tx,ty])
    return graph

n,m = map(int,sys.stdin.readline().split())
graph = []
r_graph=[]
check1=0
for i in range(m):
    graph.append(list(map(int,sys.stdin.readline().split())))
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if j == 0:
            check1+=1
arr1 = bfs(graph)
check = -1
max1 = -9876543251
for i in arr1:
    if max(i)>=max1:
        max1 = max(i)
    for j in i:
        if j==0:
            check =0
            break
if check1 == 0:
    print(0)
elif check == 0:
    print(-1)
else:
    print(max1-1)
