def check_only_one_num(n, grid):
    only_one, only_zero = False, False

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
    else:
        return False

def bfs(grid, n, i, j, visited, moves, root):
    visited[i][j] = True
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

    for x, y in path:
        grid[x][y] = area
        root[x][y] = (n*i + j)

def get_area(grid, n, i, j, root, moves):
    check_root = set()
    area = 1

    for move in moves:
        nx = i + move[0]
        ny = j + move[1]

        if 0<=nx<n and 0<=ny<n and grid[nx][ny] != 0:
            r = root[nx][ny]
            if r not in check_root:
                check_root.add(r)
                area += grid[nx][ny]
    
    return area

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        check = check_only_one_num(n, grid)
        if check != False:
            return check

        moves = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = [[False]*n for _ in range(n)]
        root = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    bfs(grid, n, i, j, visited, moves, root)
        
        answer = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    area = get_area(grid, n, i, j, root, moves)
                    answer = max(answer, area)

        return answer