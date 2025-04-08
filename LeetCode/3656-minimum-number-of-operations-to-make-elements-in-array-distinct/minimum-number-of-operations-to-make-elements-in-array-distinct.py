class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums_set = set()

        for i in range(n-1, -1, -1):
            if nums[i] in nums_set:
                return i // 3 + 1            
            nums_set.add(nums[i])
        
        return 0