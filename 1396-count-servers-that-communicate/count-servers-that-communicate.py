class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque([])
        
        row = [[] for _ in range(n)]
        col = [[] for _ in range(m)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j))
        
        moves = [[0,1], [0,-1], [1,0], [-1,0]]
        answer = 0

        while q:
            x, y = q.popleft()
            row[x].append((x,y))
            col[y].append((x,y))
        
        answer = 0
        check = defaultdict(bool)

        for i in range(n):
            if len(row[i]) >= 2:
                for loc in row[i]:
                    if not check[loc]:
                        answer += 1
                        check[loc] = True
        for i in range(m):
            if len(col[i]) >= 2:
                for loc in col[i]:
                    if not check[loc]:
                        answer += 1
                        check[loc] = True
        
        return answer
        