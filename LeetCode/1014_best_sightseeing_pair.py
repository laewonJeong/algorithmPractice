class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        answer = 0
        n = len(values)
        dp = [0 for _ in range(n)]
        dp[0] = values[0]

        for i in range(1, n):
            answer = max(answer, dp[i-1] + values[i] - i)
            dp[i] = max(dp[i-1], values[i] + i)

        return answer
