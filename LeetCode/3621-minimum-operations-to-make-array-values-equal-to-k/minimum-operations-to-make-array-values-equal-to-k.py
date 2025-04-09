class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        
        nums = set(nums)

        return len(nums) if k not in nums else len(nums)-1