class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        path = [[] for _ in range(numCourses)]

        for v1, v2 in prerequisites:
            graph[v1].append(v2)
        
        for i in range(numCourses):
            q = deque([i])
            visited = [False] * numCourses
            visited[i] = True

            while q:
                vertex = q.popleft()
                path[i].append(vertex)

                for next_vertex in graph[vertex]:
                    if not visited[next_vertex]:
                        q.append(next_vertex)
                        visited[next_vertex] = True

        answer = []
        for v1, v2 in queries:
            answer.append(v2 in path[v1])
        
        return answer