class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = defaultdict(bool)
        visited[(0,0,0)] = True
        moves = [[], [0, 1], [0, -1], [1,0], [-1,0]]
        q = [(0,0,0)] 
        heapq.heapify(q)

        while q:
            cost, x, y = heapq.heappop(q)
            
            if x == n-1 and y == m-1:
                return cost

            for i in range(1, 5):
                nx = x + moves[i][0]
                ny = y + moves[i][1]
                if 0<= nx < n and 0<=ny<m:
                    if i == grid[x][y]:
                        if not visited[(cost, nx, ny)]:
                            visited[(cost, nx, ny)] = True
                            heapq.heappush(q, (cost, nx, ny))
                    else:
                        if not visited[(cost+1, nx, ny)]:
                            visited[(cost+1, nx, ny)] = True
                            heapq.heappush(q, (cost+1, nx, ny))