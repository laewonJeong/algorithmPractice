class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        count = [0] * (n**2+1)

        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1
        
        repeat_num = -1
        missing_num = -1
        for i in range(1, n**2+1):
            if count[i] == 0:
                missing_num = i
            elif count[i] == 2:
                repeat_num = i
        
        return [repeat_num, missing_num]