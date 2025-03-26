class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        check = -1
        n = len(grid)
        m = len(grid[0])
        new_grid = []

        for i in range(n):
            for j in range(m):
                new_grid.append(grid[i][j])
                if check == -1:
                    check = grid[i][j] % x
                elif check != grid[i][j] % x:
                    return -1
        
        new_grid.sort()

        answer = 0
        target = new_grid[(n * m) // 2]
        for num in new_grid:
            answer += abs(target - num) // x

        return answer