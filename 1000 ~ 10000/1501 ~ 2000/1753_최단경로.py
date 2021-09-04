import sys
import heapq

v,e=map(int,sys.stdin.readline().split())
s = int(sys.stdin.readline())
g=[[] for _ in range(v+1)]

def dijkstra(graph, start):
    distances = [987654321]*(v+1)
    distances[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    while q:
        current_distance, current_destination = heapq.heappop(q)
        if distances[current_destination] < current_distance:
            continue
        for next_node, weight in graph[current_destination]:
            next_weight = weight + current_distance
            if next_weight < distances[next_node]:
                distances[next_node] = next_weight
                heapq.heappush(q, [next_weight, next_node])
    return distances

for i in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    g[a].append((b,c))
r = dijkstra(g,s)
for i in range(1,len(r)):
    if r[i] == 987654321:
        print("INF")
    else:
        print(r[i])