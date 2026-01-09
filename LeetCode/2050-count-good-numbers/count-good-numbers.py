class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = (n+1) // 2
        odd = n // 2
        mod = 10 ** 9 + 7

        def fast_pow(x, y):
            if y == 0:
                return 1
            half = fast_pow(x, y // 2)
            if y % 2 == 0:
                return (half * half) % mod
            else:
                return (half * half * x) % mod

        return ((fast_pow(5, even)) * (fast_pow(4, odd))) % mod