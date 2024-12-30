class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [0 for _ in range(high+1)]
        dp[0] = 1
        answer = 0

        for i in range(1, high+1):
            if i >= zero:
                dp[i] = dp[i] + dp[i-zero] % mod
            if i >= one:
                dp[i] = dp[i] + dp[i-one] % mod
        
            if low<=i<=high:
                answer += dp[i]
        
        return answer % mod