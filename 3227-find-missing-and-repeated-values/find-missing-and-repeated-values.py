class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        sum_n = ((n*n) * (n*n + 1))//2

        check = set()

        repeat_num = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] in check:
                    repeat_num = grid[i][j]
                else:
                    check.add(grid[i][j])
                    sum_n -= grid[i][j]

        return [repeat_num, sum_n]
            