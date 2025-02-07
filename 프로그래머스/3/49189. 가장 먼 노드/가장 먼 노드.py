import heapq
def dijkstra(graph, start, n):
    d = [float('inf')] * n
    d[start] = 0
    hq = []
    heapq.heappush(hq, [0, start])
    
    while hq:
        now_d, now_v = heapq.heappop(hq)
        
        if now_d > d[now_v]: continue
        
        for next_v, w in graph[now_v]:
            new_d = now_d + w
            if d[next_v] > new_d:
                d[next_v] = new_d
                heapq.heappush(hq, [new_d, next_v])
    
    return d

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n)]
    
    for v1, v2 in edge:
        graph[v1-1].append([v2-1, 1])
        graph[v2-1].append([v1-1, 1])

    d = dijkstra(graph, 0, n)
    
    return d.count(max(d))