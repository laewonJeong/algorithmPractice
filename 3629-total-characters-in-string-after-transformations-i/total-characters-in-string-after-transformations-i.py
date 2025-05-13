class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7
        dp = [1] * 26

        for _ in range(t):
            temp = [0] * 26
            for i in range(25):
                temp[i] = dp[i + 1] % mod
            temp[25] = (dp[0] + dp[1]) % mod
            dp = temp

        result = 0
        for ch in s:
            result += dp[ord(ch) - 97] % mod

        return result % mod