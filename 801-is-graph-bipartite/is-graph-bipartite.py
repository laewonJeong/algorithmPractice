class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        color = [-1 for _ in range(n)]


        for i in range(n):
            if color[i] != -1:
                continue
            
            q= deque([i])

            while q:
                vertex = q.popleft()

                for next_vertex in graph[vertex]:
                    if color[next_vertex] == -1:
                        color[next_vertex] = 1 if color[vertex] == 0 else 0
                        q.append(next_vertex)
                    elif color[next_vertex] == color[vertex]:
                        return False
        
        return True