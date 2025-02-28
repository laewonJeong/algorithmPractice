class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            local_max = max(nums[i], nums[i] + local_max)
            answer = max(answer, local_max)
        
        return answer