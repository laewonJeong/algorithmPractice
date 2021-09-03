import sys
import heapq

def dijkstra(graph, start):
    distances = [float('inf') for node in graph]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        if distances[current_destination] < current_distance:
            continue
        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return distances

n,m,x = map(int,sys.stdin.readline().split())
graph=[[] for i in range(n + 1)]
graph1=[[] for j in range(n+1)]

for _ in range(m):
    source,destination,weight = map(int,sys.stdin.readline().split())
    graph[source].append([destination,weight])
    graph1[destination].append([source,weight])
result = 0
a= dijkstra(graph,x)
b= dijkstra(graph1,x)
for j in range(1,n+1):
    if a[j]+b[j]>result:
        result = a[j]+b[j]
print(result)