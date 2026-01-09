class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        COLORS = [0, 1, 2]

        def is_valid(col):
            for i in range(1, len(col)):
                if col[i] == col[i - 1]:
                    return False
            return True

        valid_cols = []
        for col in product(COLORS, repeat=m):
            if is_valid(col):
                valid_cols.append(col)

        neighbors = {}
        for c1 in valid_cols:
            neighbors[c1] = []
            for c2 in valid_cols:
                if all(x != y for x, y in zip(c1, c2)):
                    neighbors[c1].append(c2)

        dp = {}
        for col in valid_cols:
            dp[col] = 1

        for _ in range(n - 1):
            new_dp = {}
            for col in valid_cols:
                new_dp[col] = 0
                for prev in neighbors[col]:
                    new_dp[col] = (new_dp[col] + dp[prev]) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD
