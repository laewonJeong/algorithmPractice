def get_answer(row_or_col, n, s):
    for i in range(n):
        if len(row_or_col[i]) >= 2:
            for loc in row_or_col[i]:
                s.add(loc)

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        check = defaultdict(bool)

        row = [[] for _ in range(n)]
        col = [[] for _ in range(m)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row[i].append((i,j))
                    col[j].append((i,j))
        
        s = set()
        get_answer(row, n, s)
        get_answer(col, m, s)
        
        return len(s)
        