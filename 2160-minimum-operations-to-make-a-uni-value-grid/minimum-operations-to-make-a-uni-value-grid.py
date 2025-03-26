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

        if (n * m) % 2 == 1:
            answer = 0
            target = new_grid[(n * m) // 2]
            for num in new_grid:
                answer += abs(target - num) // x

            return answer
        else:
            target1 = new_grid[(n * m) // 2]
            target2 = new_grid[(n * m) // 2 - 1]
            answer = [0, 0]
            for num in new_grid:
                answer[0] += abs(target1 - num) // x
                answer[1] += abs(target2 - num) // x
            
            return min(answer)