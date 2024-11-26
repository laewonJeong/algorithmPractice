class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0

        graph = [[] for _ in range(n)]

        for v1, v2 in edges:
            graph[v1].append(v2)

        for i in range(n):
            while True:
                before_len = len(graph[i])
                for v in graph[i]:
                    for vv in graph[v]:
                        if vv not in graph[i]:
                            graph[i].append(vv)
                if len(graph[i]) == n-1:
                    return i
                if before_len == len(graph[i]):
                    break

        return -1
