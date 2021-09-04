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

n,m = map(int,sys.stdin.readline().split())
graph=[[] for i in range(n + 1)]

for _ in range(m):
    source,destination,weight = map(int,sys.stdin.readline().split())
    graph[source].append([destination,weight])
    graph[destination].append([source,weight])
a,b = map(int,sys.stdin.readline().split())
x = dijkstra(graph,1)
y = dijkstra(graph,a)
z = dijkstra(graph,b)
min1 = x[a]+y[b]+z[n]
min2 = x[b]+z[a]+y[n]
if min1 == float('inf') and min2 == float('inf'):
    print(-1)
else:
    print(min(min1,min2))