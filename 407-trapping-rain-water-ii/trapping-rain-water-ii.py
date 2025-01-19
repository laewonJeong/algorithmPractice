class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        
        if n < 3 or m < 3:
            return 0
        
        visited = [[False] * m for _ in range(n)]
        q = []
        
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n-1 or j == 0 or j == m-1:
                    heapq.heappush(q, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        answer = 0
        
        while q:
            height, x, y = heapq.heappop(q)
            
            for move in moves:
                nx, ny = x + move[0], y + move[1]
                
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    answer += max(0, height - heightMap[nx][ny])
                    heapq.heappush(q, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True
        
        return answer
