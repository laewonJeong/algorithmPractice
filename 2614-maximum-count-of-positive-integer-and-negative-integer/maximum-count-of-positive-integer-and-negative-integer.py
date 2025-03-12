class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        return max(n - bisect_left(nums, 1), bisect_right(nums,-1))