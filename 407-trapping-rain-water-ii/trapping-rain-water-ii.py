class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        answer = 0

        visited = defaultdict(bool)
        moves = [[0,1],[0,-1],[1,0],[-1,0]]
        q = []
        
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n-1 or j == 0 or j == m-1:
                    heapq.heappush(q, (heightMap[i][j], i, j))
                    visited[(i, j)] = True
        
        while q:
            height, x, y = heapq.heappop(q)

            for move in moves:
                nx = x + move[0]
                ny = y + move[1]

                if 0 <= nx < n and 0 <= ny < m and not visited[(nx, ny)]:
                    visited[(nx, ny)] = True
                    if heightMap[nx][ny] < height:
                        answer += height - heightMap[nx][ny]
                        heightMap[nx][ny] = height
                    heapq.heappush(q, (heightMap[nx][ny], nx, ny))

        return answer