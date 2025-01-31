def bfs(grid, n, i, j, visited, moves):
    q = deque([(i,j)])
    area = 0
    path = []

    while q:
        x, y = q.popleft()
        area+=1
        path.append((x, y))

        for move in moves:
            nx = x + move[0]
            ny = y + move[1]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
    
    return path, area

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        moves = [[0,1], [0,-1], [1,0], [-1,0]]
        answer = 0
        visited = [[False]*n for _ in range(n)]
        root = [[0]*n for _ in range(n)]

        only_one = False
        only_zero = False

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    only_zero = True
                else:
                    only_one = True
        
        if only_zero and not only_one:
            return 1
        elif not only_zero and only_one:
            return n*n


        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    path, area = bfs(grid, n, i, j, visited, moves)
                    for x, y in path:
                        grid[x][y] = area
                        root[x][y] = (n*i + j)
        
        visited = [False]*(n*n)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    area = 1
                    r_loc = []
                    for move in moves:
                        nx = i + move[0]
                        ny = j + move[1]

                        if 0<=nx<n and 0<=ny<n and grid[nx][ny] != 0:
                            n_area = grid[nx][ny]
                            r = root[nx][ny]
                            if not visited[r]:
                                r_loc.append(r)                            
                                visited[r] = True
                                area += n_area
                    for loc in r_loc:
                        visited[loc] = False

                    answer = max(answer, area)

        return answer