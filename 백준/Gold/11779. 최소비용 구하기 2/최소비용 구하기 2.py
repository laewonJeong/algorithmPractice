import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2, cost = map(int, input().split())
    graph[v1-1].append([v2-1, cost])

start, end = map(int, input().split())

def dijkstra(start):
    distances = [[float('inf'), []] for _ in range(n)]
    distances[start-1] = [0, [start]]
    q = []
    heapq.heappush(q, (0, start-1, [start]))

    while q:
        distance, now, path = heapq.heappop(q)
        if distances[now][0] < distance:
            continue
            
        for next in graph[now]:
            cost = distance + next[1]
            if cost < distances[next[0]][0]:
                distances[next[0]][0] = cost
                distances[next[0]][1] = path + [next[0]+1]
                heapq.heappush(q, (cost, next[0], distances[next[0]][1]))
    return distances

answer = dijkstra(start)[end-1]
print(answer[0])
print(len(answer[1]))
print(*answer[1])