class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges)

        graph = [[] for _ in range(n+1)]

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        bob_path = {}

        def find_bob_path(visited, path, now):
            nonlocal bob_path

            if now == 0:
                for i, node in enumerate(path):
                    bob_path[node] = i
                return
            if 0 in bob_path:
                return

            for next_vertex in graph[now]:
                if not visited[next_vertex]:
                    visited[next_vertex] = True
                    path.append(next_vertex)

                    find_bob_path(visited, path, next_vertex)

                    path.pop()
                    visited[next_vertex] = False

        visited = [False] * (n+1)
        visited[bob] = True
        find_bob_path(visited, [bob], bob)

        answer = float('-inf')
        def dfs_alice(node, depth, visited, income):
            nonlocal answer

            if node in bob_path and depth == bob_path[node]:
                income += amount[node]//2
            elif (node in bob_path and depth < bob_path[node]) or node not in bob_path:
                income += amount[node]

            if node != 0 and len(graph[node]) == 1:
                answer = max(answer, income)
                return

            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    dfs_alice(next_node, depth+1, visited, income)
                    visited[next_node] = False

        visited = [False] * (n+1)
        visited[0] = True
        dfs_alice(0, 0, visited, 0)

        return answer