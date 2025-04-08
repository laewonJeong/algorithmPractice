class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n, 3):
            if n - i == len(set(nums[i:])):
                return i // 3
        
        return (i+3)//3