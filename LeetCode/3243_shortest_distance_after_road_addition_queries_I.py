def dijkstra(graph, n, start):
    distances = [float(inf) for _ in range(n)]
    distances[start] = 0
    pq = [[0, start]]

    while pq:
        current = heapq.heappop(pq)
        if current[0] > distances[current[1]]:
            continue
        for to, distance in graph[current[1]]:
            now_distance = current[0] + distance
            if now_distance < distances[to]:
                distances[to] = now_distance
                heapq.heappush(pq, [now_distance, to])
    
    return distances[-1]

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        answer = []

        for i in range(1, n):
            graph[i-1].append([i,1])
        
        for u, v in queries:
            graph[u].append([v,1])
            answer.append(dijkstra(graph, n, 0))
        
        return answer
