class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(len(nums) - bisect_left(nums, 1), bisect_right(nums,-1))