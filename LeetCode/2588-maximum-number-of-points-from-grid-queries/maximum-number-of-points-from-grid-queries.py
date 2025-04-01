class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        answer = [0] * len(queries)

        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])
        visited = [[0] * m for _ in range(n)]

        hq = []
        heapq.heappush(hq, (grid[0][0], 0, 0))
        visited[0][0] = 1
        cnt = 0

        for query, i in sorted_queries:
            while hq and hq[0][0] < query:
                now, x, y = heapq.heappop(hq)
                cnt += 1

                for move in moves:
                    nx = x + move[0]
                    ny = y + move[1]

                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        heapq.heappush(hq, (grid[nx][ny], nx, ny))
            answer[i] = cnt

        return answer