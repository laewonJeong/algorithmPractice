import sys
import heapq

def dijkstra(graph,start):
    distance=[float('inf') for i in range(n+1)]
    distance[start] = 0
    hq = []
    heapq.heappush(hq,[distance[start],start])
    while hq:
        a,b = heapq.heappop(hq)
        if distance[b] < a:
            continue
        for x,y in graph[b]:
            dis = a+y
            if dis < distance[x]:
                distance[x] = dis
                heapq.heappush(hq,[dis,x])
    return distance
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph=[[] for i in range(n+1)]

for _ in range(m):
    source, dest, weight = map(int,sys.stdin.readline().split())
    graph[source].append([dest,weight])
start,end = map(int,sys.stdin.readline().split())
print(dijkstra(graph,start)[end])