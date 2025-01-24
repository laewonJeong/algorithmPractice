class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        graph_reverse = [[] for _ in range(n)]
        q = deque([])
        answer = []

        for i in range(n):
            if len(graph[i]) == 0:
                q.append(i)
            for v in graph[i]:
                graph_reverse[v].append(i)
        
        while q:
            vertex = q.popleft()
            answer.append(vertex)
            
            for v in graph_reverse[vertex]:
                graph[v].remove(vertex)
                if len(graph[v]) == 0:
                    q.append(v)
        
        return sorted(answer)