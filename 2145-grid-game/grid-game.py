class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix = [[0 for _ in range(n)] for _ in range(2)]
        prefix[0][0] = grid[0][0]
        prefix[1][0] = grid[1][0]

        for i in range(1, n):
            prefix[0][i] = prefix[0][i-1] + grid[0][i]
            prefix[1][i] = prefix[1][i-1] + grid[1][i]
        
        answer = 9876543210
        for i in range(n):
            can_blue1 = prefix[0][-1] - prefix[0][i]
            if i != 0:
                can_blue2 = prefix[1][i-1]
            else:
                can_blue2 = 0

            blue_points = max(can_blue1, can_blue2)
            answer = min(answer, blue_points)
            
        return answer