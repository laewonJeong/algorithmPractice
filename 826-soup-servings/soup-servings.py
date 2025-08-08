class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0

        n = math.ceil(n / 25)
        dp = [[0.0] * (n + 1) for _ in range(n + 1)]

        for a in range(n + 1):
            for b in range(n + 1):
                if a == 0 and b == 0:
                    dp[a][b] = 0.5
                elif a == 0:
                    dp[a][b] = 1.0
                elif b == 0:
                    dp[a][b] = 0.0
                else:
                    dp[a][b] = 0.25 * (
                        dp[max(a-4, 0)][b] +
                        dp[max(a-3, 0)][max(b-1, 0)] +
                        dp[max(a-2, 0)][max(b-2, 0)] +
                        dp[max(a-1, 0)][max(b-3, 0)]
                    )

        return dp[n][n]
