class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        local_max = nums[0]
        global_max = nums[0]
        local_min = nums[0]
        global_min = nums[0]

        for i in range(1, len(nums)):
            local_max = max(nums[i], nums[i] + local_max)
            global_max = max(global_max, local_max)

            local_min = min(nums[i], nums[i] + local_min)
            global_min = min(global_min, local_min)
        
        if global_max < 0:
            global_max *= -1
        if global_min < 0:
            global_min *= -1

        return max(global_max, global_min)