class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        local_max = nums[0]
        local_min = nums[0]
        answer = abs(nums[0])

        for i in range(1, len(nums)):
            local_max = max(nums[i], nums[i] + local_max)
            local_min = min(nums[i], nums[i] + local_min)

            answer = max(answer, abs(local_max), abs(local_min))

        return answer