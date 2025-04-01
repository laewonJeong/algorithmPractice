class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            point, brain_power = questions[i]
            next_idx = i + brain_power + 1

            if next_idx < n:
                dp[i] = dp[next_idx] + point
            else:
                dp[i] = point
            
            dp[i] = max(dp[i], dp[i+1])

        return dp[0]


