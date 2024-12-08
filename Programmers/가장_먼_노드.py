import heapq

def dijkstra(start, graph):
    d = [987654321 for _ in range(len(graph))]
    d[start] = 0
    hq = []
    heapq.heappush(hq, [d[start], start])
    
    while hq:
        now_d, now_v = heapq.heappop(hq)
        
        if d[now_v] < now_d: continue
        
        for next_vertex in graph[now_v]:
            new_d = now_d + 1
            if new_d < d[next_vertex]:
                d[next_vertex] = new_d
                heapq.heappush(hq, [new_d, next_vertex])
    return d

def solution(n, edge):
    graph = [[] for _ in range(n)]
    
    for s, e in edge:
        graph[s-1].append(e-1)
        graph[e-1].append(s-1)
    
    answer = dijkstra(0, graph)
    
    return answer.count(max(answer))
