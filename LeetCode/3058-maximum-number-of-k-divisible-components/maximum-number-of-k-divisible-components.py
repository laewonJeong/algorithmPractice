def recursion(graph, visited, node, values, k):
    total = values[node]
    components = 0

    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            sub_total, sub_components = recursion(graph, visited, next_node, values, k)
            total += sub_total

            if sub_total % k == 0:
                components += sub_components + 1
            else:
                components += sub_components

    return total, components

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        visited = defaultdict(bool)
        visited[0] = True

        _, components = recursion(graph, visited, 0, values, k)
        return components + 1
