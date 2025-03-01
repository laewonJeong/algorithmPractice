import sys
import heapq

input = sys.stdin.readline

def dijkstra(start, n, graph):
    INF = float('inf')
    dist = [INF] * n
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        cost, node = heapq.heappop(pq)
        
        if cost > dist[node]:
            continue
        
        for neighbor in graph[node]:
            new_cost = cost + 1
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
    
    return sum(dist)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1-1].append(v2-1)
    graph[v2-1].append(v1-1)

min_kevin = float('inf')
answer = 0

for i in range(n):
    kevin = dijkstra(i, n, graph)
    if kevin < min_kevin:
        min_kevin = kevin
        answer = i + 1

print(answer)