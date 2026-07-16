class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n          = len(nums)
        mx         = [nums[0]] * n
        prefix_gcd = [0] * n

        for i in range(1, n):
            mx[i] = max(mx[i-1] , nums[i])

        for i, num in enumerate(nums):
            prefix_gcd[i] = gcd(nums[i], mx[i])

        prefix_gcd.sort()
        answer = 0
        for i in range(1, n//2 + 1):
            answer += gcd(prefix_gcd[i-1], prefix_gcd[-i])

        return answer