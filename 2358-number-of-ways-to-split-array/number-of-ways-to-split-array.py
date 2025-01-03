class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0

        left = 0
        right = sum(nums)

        for i in range(n-1):
            left += nums[i]
            right -= nums[i]

            if left >= right:
                answer += 1
        
        return answer