import sys
import heapq

def dijkstra(graph,start):
    distance = [float('inf') for i in range(n+1)]
    check = [0 for i in range(n+1)]
    distance[start] = 0
    hq = []
    heapq.heappush(hq,[distance[start],start])
    total = 0
    while hq:
        a,b = heapq.heappop(hq)
        if a <= m and check[b]==0:
            total += item[b]
            check[b]=1
        if distance[b] < a:
            continue
        for new_destination, new_distance in graph[b]:
            dis = a + new_distance
            if dis < distance[new_destination]:
                distance[new_destination] = dis
                heapq.heappush(hq, [dis, new_destination])
    return total

n,m,r = map(int,sys.stdin.readline().split())
a = sys.stdin.readline().split()
item=[0]*(n+1)
for i in range(1,len(a)+1):
    item[i] = int(a[i-1])
graph=[[] for i in range(n+1)]
for _ in range(r):
    s,d,w = map(int,sys.stdin.readline().split())
    graph[s].append([d,w])
    graph[d].append([s,w])
result = 0
for i in range(1,n+1):
    a = dijkstra(graph,i)
    if(result<a):
        result = a
print(result)