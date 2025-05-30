class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dijkstra(start, graph):
            distances = [float('inf')] * len(graph)
            distances[start] = 0
            hq = []
            heapq.heappush(hq, (0, start))
    
            while hq:
                now_d, now_v = heapq.heappop(hq)
        
                if now_d > distances[now_v]:
                    continue
        
                for next_v in graph[now_v]:
                    new_d = now_d + 1
            
                    if new_d < distances[next_v]:
                        distances[next_v] = new_d
                        heapq.heappush(hq, (new_d, next_v))
    
            return distances


        n = len(edges)
        graph = [[] for _ in range(n)]

        for i in range(n):
            if edges[i] != -1:
                graph[i].append(edges[i])


        distances1 = dijkstra(node1, graph)
        distances2 = dijkstra(node2, graph)

        check = float('inf')
        answer = -1

        for i in range(n):
            max_dis = max(distances1[i], distances2[i]) 
            if max_dis < check:
                check = max_dis
                answer = i
        
        return answer