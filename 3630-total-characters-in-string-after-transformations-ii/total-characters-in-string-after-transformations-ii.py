MOD = 10**9 + 7

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        def mat_mult(A, B):
            size = len(A)
            result = [[0]*size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if A[i][k]:
                        for j in range(size):
                            result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
            return result

        def mat_pow(mat, power):
            size = len(mat)
            result = [[int(i == j) for j in range(size)] for i in range(size)]
            while power:
                if power % 2:
                    result = mat_mult(result, mat)
                mat = mat_mult(mat, mat)
                power //= 2
            return result

        T = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(1, nums[i] + 1):
                next_char = (i + j) % 26
                T[next_char][i] += 1

        dp = [0] * 26
        for c in s:
            dp[ord(c) - ord('a')] += 1

        T_t = mat_pow(T, t)

        result = 0
        for i in range(26):
            for j in range(26):
                result = (result + T_t[i][j] * dp[j]) % MOD

        return result
