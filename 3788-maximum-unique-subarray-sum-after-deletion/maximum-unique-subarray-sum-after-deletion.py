class Solution:
    def maxSum(self, nums: List[int]) -> int:

        if min(nums) < 0 and max(nums) < 0:
            return max(nums)

        new_nums = []

        for num in nums:
            if num not in new_nums and num > 0:
                new_nums.append(num)
        
        return sum(new_nums)
                