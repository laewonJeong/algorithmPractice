class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        dp = [0 for _ in range(n+1)]
        dp[1], dp[2], dp[3] = 1, 2, 3

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]