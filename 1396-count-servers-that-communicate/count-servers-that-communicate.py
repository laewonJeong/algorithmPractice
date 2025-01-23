def get_answer(row_or_col, n, check):
    answer = 0
    for i in range(n):
        if len(row_or_col[i]) >= 2:
            for loc in row_or_col[i]:
                if not check[loc]:
                    answer += 1
                    check[loc] = True
    return answer

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        answer = 0
        check = defaultdict(bool)

        row = [[] for _ in range(n)]
        col = [[] for _ in range(m)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row[i].append((i,j))
                    col[j].append((i,j))

        answer += get_answer(row, n, check)
        answer += get_answer(col, m, check)
        
        return answer
        