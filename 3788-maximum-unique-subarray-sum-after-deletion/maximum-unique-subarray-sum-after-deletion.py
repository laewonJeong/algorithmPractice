class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)

        nums = set(list(nums))
        answer = 0
        for num in nums:
            if num > 0:
                answer += num
        
        return answer
                