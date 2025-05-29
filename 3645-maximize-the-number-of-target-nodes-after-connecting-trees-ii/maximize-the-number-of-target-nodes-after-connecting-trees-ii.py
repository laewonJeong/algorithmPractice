class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def build_graph(edges, n):
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def get_parity_counts(graph):
            n = len(graph)
            level = [-1] * n
            q = deque()
            q.append(0)
            level[0] = 0
            even_count = 1
            odd_count = 0

            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if level[neighbor] == -1:
                        level[neighbor] = level[node] + 1
                        if level[neighbor] % 2 == 0:
                            even_count += 1
                        else:
                            odd_count += 1
                        q.append(neighbor)
            return level, even_count, odd_count

        n = len(edges1) + 1
        m = len(edges2) + 1

        graph1 = build_graph(edges1, n)
        graph2 = build_graph(edges2, m)

        level1, even1, odd1 = get_parity_counts(graph1)
        level2, even2, odd2 = get_parity_counts(graph2)

        answer = []
        for i in range(n):
            my_parity = level1[i] % 2
            if my_parity == 0:
                count_in_t1 = even1
            else:
                count_in_t1 = odd1
            count_in_t2 = max(even2, odd2)
            answer.append(count_in_t1 + count_in_t2)

        return answer
