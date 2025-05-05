class Solution:
    def numTilings(self, n: int) -> int:
        #0,1,2,5,11,24,53
        mod = 10**9 + 7
        if n == 1: return 1
        elif n == 2: return 2

        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n+1):
            dp[i] = (dp[i-1] * 2 + dp[i-3]) % mod
        
        return dp[n]