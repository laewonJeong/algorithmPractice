import heapq

def dijkstra(start, graph):
    distances = [float('inf')] * len(graph)
    distances[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        distance, now = heapq.heappop(q)
        if distance > distances[now]:
            continue
        
        for next, d in graph[now]:
            new_d = distance + d
            if new_d < distances[next]:
                distances[next] = new_d
                heapq.heappush(q, (new_d, next))
    return distances

def solution(n, edge):
    graph = [[] for _ in range(n)]
    
    for s, e in edge:
        graph[s-1].append([e-1,1])
        graph[e-1].append([s-1,1])
    
    answer = dijkstra(0, graph)
    
    return answer.count(max(answer))