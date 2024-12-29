class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        start_x, start_y = 0, 0
        
        if grid[start_x][start_y] == 1:
            health -= 1
            if health == 0:
                return False

        n = len(grid)
        m = len(grid[0])

        moves = [[0,1], [1,0], [0,-1], [-1,0]]
        visited = defaultdict(bool)
        visited[(start_x, start_y)] = True
        q = []
        heapq.heappush(q, (-health, start_x, start_y))

        while q:
            h, x, y = heapq.heappop(q)
            
            if x == n-1 and y == m-1:
                return True
            
            for move in moves:
                nx = x + move[0]
                ny = y + move[1]

                if 0 <= nx < n and 0 <= ny < m and not visited[(nx, ny)]:
                    visited[(nx, ny)] = True
                    if grid[nx][ny] == 1:
                        if -h > 1:
                            heapq.heappush(q, (h+1, nx, ny))
                        else:
                            visited[(nx, ny)] = False
                    else:
                        heapq.heappush(q, (h, nx, ny))

        return False