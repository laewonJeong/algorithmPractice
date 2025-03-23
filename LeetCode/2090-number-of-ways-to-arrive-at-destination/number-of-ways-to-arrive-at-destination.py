class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for v1, v2, cost in roads:
            graph[v1].append([v2, cost])
            graph[v2].append([v1, cost])

        def dijkstra(start, graph, n):
            distances = [float('inf')] * n
            distances[start] = 0
            hq = []
            heapq.heappush(hq, (0, start))
            path_cnt = [0] * n
            path_cnt[0] = 1

            while hq:
                now_d, now_v = heapq.heappop(hq)
                if now_d > distances[now_v]:
                    continue
                
                for next_v, d in graph[now_v]:
                    new_d = d + now_d
                    if new_d < distances[next_v]:
                        distances[next_v] = new_d
                        path_cnt[next_v] = path_cnt[now_v]
                        heapq.heappush(hq, (new_d, next_v))
                    elif new_d == distances[next_v]:
                        path_cnt[next_v] = (path_cnt[next_v] + path_cnt[now_v]) % (10 ** 9 + 7)
            return path_cnt[-1]

        return dijkstra(0, graph, n)