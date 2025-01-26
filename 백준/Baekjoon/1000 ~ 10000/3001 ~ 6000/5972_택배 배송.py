import sys
import heapq

def dijkstra(graph,start):
    distance = [float('inf') for i in range(n+1)]
    distance[start] = 0
    hq = []
    heapq.heappush(hq,[distance[start],start])
    total = 0
    while hq:
        a,b = heapq.heappop(hq)
        if distance[b] < a:
            continue
        for new_destination, new_distance in graph[b]:
            dis = a + new_distance
            if dis < distance[new_destination]:
                distance[new_destination] = dis
                heapq.heappush(hq, [dis, new_destination])
    return distance

n,m = map(int,sys.stdin.readline().split())

graph=[[] for i in range(n+1)]
for _ in range(m):
    s,d,w = map(int,sys.stdin.readline().split())
    graph[s].append([d,w])
    graph[d].append([s,w])
a = dijkstra(graph,1)
print(a[n])