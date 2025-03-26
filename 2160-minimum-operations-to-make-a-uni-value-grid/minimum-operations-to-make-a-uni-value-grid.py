class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        check = -1
        new_grid = [num for row in grid for num in row]
        n = len(new_grid)
        check = new_grid[0] % x

        for i in range(1, n):
            if new_grid[i] % x != check:
                return -1

        new_grid.sort()

        answer = 0
        target = new_grid[n // 2]
        for num in new_grid:
            answer += abs(target - num) // x

        return answer