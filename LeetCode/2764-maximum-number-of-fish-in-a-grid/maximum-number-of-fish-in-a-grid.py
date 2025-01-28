class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        moves = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = [[False] * m for _ in range(n)]
        answer = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    q = deque([])
                    q.append((i,j))
                    visited[i][j] = True

                    fish = 0
                    while q:
                        x, y = q.popleft()
                        fish += grid[x][y]

                        for move in moves:
                            nx = x + move[0]
                            ny = y + move[1]

                            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != 0:
                                visited[nx][ny] = True
                                q.append((nx, ny))

                    answer = max(answer, fish)
        
        return answer