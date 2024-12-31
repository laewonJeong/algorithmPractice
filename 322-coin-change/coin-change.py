class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [float('inf') for _ in range(amount+1)]

        for i in range(1, amount+1):
            if i in coins:
                dp[i] = 1
            else:
                for coin in coins:
                    if i-coin > 0:
                        dp[i] = min(dp[i], dp[i-coin] + dp[coin])

        #print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1